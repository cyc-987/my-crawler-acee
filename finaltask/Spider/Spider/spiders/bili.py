import scrapy
import re
import js2xml
import json
from Spider.items import biliitem


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["api.bilibili.com"]
    '''
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
        'Cookie':"header_theme_version=CLOSE; home_feed_column=4; i-wanna-go-back=-1; innersign=0; CURRENT_FNVAL=4048; b_lsid=A9E5D2E5_187073C905C; bp_video_offset_364122146=775387364054794400; PVID=1; sid=7cyzvkn9; buvid4=68A1E4B4-7786-62B9-2AD7-07FD9DE3FFBF53918-022100122-yW9JSiNaa2owPj%2BD5wQFkw%3D%3D; buvid_fp=3a4cf84c849fdc6ca5055490e0f0af2a; buvid_fp_plain=undefined; fingerprint=3a4cf84c849fdc6ca5055490e0f0af2a; CURRENT_QUALITY=120; b_ut=5; DedeUserID=364122146; DedeUserID__ckMd5=19efbfb21c93a9dd; SESSDATA=af997a8d%2C1686138401%2C9a299%2Ac2; bili_jct=1ef95cc58507393c8cdbb878c4bdbbbe; rpdid=|(YYl~RmJJY0J'uYY)lmYmY); _uuid=D31955BA-3646-EFB2-5BE6-D23E5FC4435379032infoc; b_nut=100; LIVE_BUVID=AUTO4516556261469536; nostalgia_conf=-1; buvid3=A4C1A134-970E-617A-5015-011389B8D0B591887infoc"}
    '''
    start_urls = ["https://api.bilibili.com/x/web-interface/wbi/search/type?&page_size=42&keyword=ikun&search_type=video&page=%s"
                    %s for s in range(1,35)]
    
    


    def parse(self, response):
        
        udata = json.loads(response.text)       
        item = biliitem()
        p1data = udata['data']
        data = p1data['result']
        for result in data:            
            
            bvid = result['bvid']
            title = result['title']
            author = result['author']
            play = result['play']
            like = result['like']
            favorites = result['favorites']
            tag = result['tag']
            duration = result['duration']
            
            item['bvid'] = bvid
            item['title'] = title
            item['author'] = author
            item['play'] = play
            item['like'] = like
            item['duration'] = duration
            item['favorites'] = favorites
            item['tag'] = tag
            yield item        