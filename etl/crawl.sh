#!/bin/sh

scrapy crawl serlo_spider &
scrapy crawl leifi_spider &
scrapy crawl planet_schule_spider &
scrapy crawl tutory_spider &
scrapy crawl br_rss_spider &
scrapy crawl zdf_rss_spider &