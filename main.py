import argparse
import json
from crawler.crawler_arguments import CrawlerArguments
from crawler.crawler_factory import CrawlerFactory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-range", type=str, required=True)
    parser.add_argument("--end-range", type=str, required=True)
    parser.add_argument("--category", type=str, required=True)
    parser.add_argument("--crawler-type", type=str, required=True)
    parser.add_argument("--output-file-path", type=str, required=True)
    args = parser.parse_args()

    crawler_arguments = CrawlerArguments(
        start_range=args.start_range, end_range=args.end_range, category=args.category
    )
    crawler = CrawlerFactory.create_crawler(
        crawler_type=args.crawler_type, arguments=crawler_arguments
    )

    urls = crawler.crawl_urls()
    articles = crawler.crawl_articles(urls=urls)

    # Dump the list of objects to a JSON file
    with open(args.output_file_path, "w", encoding="utf-8") as json_file:
        json.dump(articles, json_file, ensure_ascii=False, indent=4)