import json
from typing import List, Dict

SITE_DATA: List[Dict[str, str]] = [
    {
        "url": "https://index-app-aiyouxi.com.cn",
        "title": "爱游戏首页",
        "keywords": "爱游戏,游戏平台,游戏社区",
        "tags": "游戏,平台,社区",
        "description": "爱游戏官方首页，提供游戏资讯、社区互动与下载服务。"
    },
    {
        "url": "https://index-app-aiyouxi.com.cn/news",
        "title": "爱游戏资讯",
        "keywords": "爱游戏,游戏新闻,行业动态",
        "tags": "新闻,资讯,游戏",
        "description": "爱游戏平台最新游戏新闻与行业动态报道。"
    },
    {
        "url": "https://index-app-aiyouxi.com.cn/download",
        "title": "爱游戏下载中心",
        "keywords": "爱游戏,游戏下载,客户端",
        "tags": "下载,客户端,游戏",
        "description": "爱游戏官方客户端下载，支持多平台安装包。"
    },
    {
        "url": "https://index-app-aiyouxi.com.cn/community",
        "title": "爱游戏社区",
        "keywords": "爱游戏,玩家社区,论坛",
        "tags": "社区,论坛,玩家",
        "description": "爱游戏玩家交流社区，分享攻略、心得与活动信息。"
    },
    {
        "url": "https://index-app-aiyouxi.com.cn/support",
        "title": "爱游戏客服支持",
        "keywords": "爱游戏,客服,帮助中心",
        "tags": "支持,客服,帮助",
        "description": "爱游戏官方客服与帮助中心，解答常见问题。"
    }
]

def format_keywords(keywords_str: str) -> List[str]:
    """将关键词字符串拆分为列表并去重"""
    return list(dict.fromkeys([kw.strip() for kw in keywords_str.split(",") if kw.strip()]))

def format_tags(tags_str: str) -> List[str]:
    """将标签字符串拆分为列表"""
    return [tag.strip() for tag in tags_str.split(",") if tag.strip()]

def generate_summary(site: Dict[str, str]) -> str:
    """生成单个站点的结构化摘要"""
    keywords_list = format_keywords(site["keywords"])
    tags_list = format_tags(site["tags"])
    summary_lines = [
        f"站点名称：{site['title']}",
        f"访问地址：{site['url']}",
        f"核心关键词：{'；'.join(keywords_list)}",
        f"标签分类：{'；'.join(tags_list)}",
        f"简要说明：{site['description']}",
        "---"
    ]
    return "\n".join(summary_lines)

def generate_all_summaries(sites: List[Dict[str, str]]) -> str:
    """生成所有站点的摘要文本"""
    parts = []
    parts.append("爱游戏平台站点结构化摘要\n")
    parts.append("=" * 40)
    for site in sites:
        parts.append(generate_summary(site))
    return "\n".join(parts)

def save_summary_to_file(content: str, filename: str = "site_summary_output.txt") -> None:
    """将摘要内容写入文本文件"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已保存至 {filename}")

def print_summary(content: str) -> None:
    """在控制台打印摘要内容"""
    print("\n生成的摘要内容：\n")
    print(content)

def main() -> None:
    """主函数：生成摘要并保存与打印"""
    summary_text = generate_all_summaries(SITE_DATA)
    print_summary(summary_text)
    save_summary_to_file(summary_text)

if __name__ == "__main__":
    main()