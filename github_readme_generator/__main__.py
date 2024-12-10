import argparse
import yaml

from github_readme_generator.handler import other, personal
from .utils import graphql
# from .handlers import personal
from .handler import repo, stats, other, followers
import os
import re


available_handlers = {
    "repo": repo.Repo,
    "stats": stats.Stats,
    "personal": personal.Personal,
    "other": other.Other,
    "followers": followers.Followers
}

class ContentGenerator:
    def __init__(self, template_string, config):
        self.template_string = template_string
        self.config = config
        self.handlers = {}

    def generate_content(self):
        pattern = re.compile(r"%{(\w+(?:\.\w+)*)}")

        def replace_func(match):
            print(f"Searching for {match.group(0)}")
            # try:
            key = match.group(1).split(".")

            cls = key[0]
            item = key[1]
            if cls in available_handlers:
                if cls not in self.handlers:
                    # need initialize
                    self.handlers[cls] = available_handlers[cls](self.config)
                print(f"Replacing {cls}.{item} with:\n {getattr(self.handlers[cls], item)}\n")
                return getattr(self.handlers[cls], item)
            print(f"Error: class {cls}  not found")
            return match.group(0)
            # except Exception as e:
            #     print(f"Error something is illegal in {match.group(0)} {e}")
            #     return match.group(0)

        result = pattern.sub(replace_func, self.template_string)
        
        return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate content based on templates and configurations.",
        epilog="Example: python -m github_readme_generator -c content.yaml -t template.md -o README.md",
    )

    parser.add_argument(
        "-c",
        "--content",
        required=True,
        help="Path to the YAML file providing content configuration. (Required)",
    )

    parser.add_argument(
        "-t",
        "--template",
        required=True,
        help="Path to the Markdown file containing the template string. (Required)",
    )


    parser.add_argument(
        "-o",
        "--out",
        default="README.md",
        help="Path to the Markdown file of the output. Defaults to 'README.md'.",
    )

    args = parser.parse_args()

    with open(args.content, "r") as f:
        config = yaml.safe_load(f)

    with open(args.template, "r") as f:
        template_string = f.read()

    
    generator = ContentGenerator(template_string, config)
    content = generator.generate_content()

    print("Finished generating content")
    print("Total used github api calls: ", graphql.QUERY.count)

    with open(args.out, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
