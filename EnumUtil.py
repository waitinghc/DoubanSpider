from enum import Enum


class InsertType(Enum):
    LATEST = 0  # 最新
    HOT = 1  # 热门
    BEST = 2  # 豆瓣250榜单电影
    ALL = 3  # 全部


class CrawlRecord(Enum):
    MOVIE = 0  # 电影
    TELEVISION = 1  # 电视
    ANIMATION = 2  # 动漫
    VARIETY = 3  # 综艺


class TagsType(Enum):
    MOVIE = "电影"
    TELEVISION = "电视剧"
    ANIMATION = "动漫"
    VARIETY = "综艺"
