from smartfile import BasicClient
import zlib

api = BasicClient('VATx6OASrU4KYLaWshrxIvyyYUIl8x','xkpKJ3Wti1cXilKJYnMSqaOLvmNnwe')

f = api.get('/path/data/', 'TemplateEmailTable.txt')

decompString = zlib.decompress(f.data, 16+zlib.MAX_WBITS)

print decompString