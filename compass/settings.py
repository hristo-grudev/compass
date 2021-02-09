BOT_NAME = 'compass'

SPIDER_MODULES = ['compass.spiders']
NEWSPIDER_MODULE = 'compass.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'compass.pipelines.CompassPipeline': 100,

}