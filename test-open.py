from TikTokApi import TikTokApi

# Watch https://www.youtube.com/watch?v=-uCt1x8kINQ for a brief setup tutorial
# with TikTokApi() as api:
#     for trending_video in api.trending.videos(count=10):
#         # Prints the author's username of the trending video.
#         print(trending_video)
#         print(trending_video.author.username)

with TikTokApi() as api: # .get_instance no longer exists
    for trending_video in api.trending.videos():
        print(trending_video)


for trending_video in api.trending.videos():
    user_stats = trending_video.author.info_full['stats']
    if user_stats['followerCount'] >= 10000:
        print(user_stats)