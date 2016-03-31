import vk_api

vk = vk_api.VkApi().get_api()

groups = [50485628]
posts = []
counter = 0
for group in groups:
    count = vk.wall.get(owner_id=-group)['count'] // 100
    for i in range(count):
        for post in vk.wall.get(owner_id=-group, offset=i * 100)['items']:
            counter += 1
            if post['text']:
                posts.append(post['text'])
        print('{0:.1f}%'.format(i / count * 100))
    print('{0:.1f}%'.format(100))
print(len(posts))
print(counter)
