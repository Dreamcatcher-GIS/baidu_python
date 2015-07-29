# BaiduMap_python
"百度地图"SDK

使用python setup.py install 进行安装

## Example
```python
from baidumap import BaiduMapClient
baiduMapClient.setAk("DW2CwL3B3271CiVyw7GdBsfR")
baiduMapClient = BaiduMapClient()

data = self.baiduMapClient.place.v2.search.get(query="银行",bounds="39.915,116.404,39.975,116.414",output="json",page_size="20")
```
data的数据就是此接口的数据:
http://api.map.baidu.com/place/v2/search?query=%E9%93%B6%E8%A1%8C&bounds=39.915,116.404,39.975,116.414&output=json&ak=E4805d16520de693a3fe707cdc962045

SDK是定制类原理,提前设置好url,通过__getattr__将属性填写进访问地址。
