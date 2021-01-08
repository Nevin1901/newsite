class Repository:
    def __init__(self, title, description, language, url, stars, imagePath):
        self.title = title
        self.description = description
        self.language = language
        self.url = url
        self.stars = stars
        self.imagePath = imagePath


#class VPSData:
#    def __init__(self, vpsName, cpuUsage, memoryUsage, storageUsage, year, month, date, hour):
#        self.vpsName = vpsName
#        self.cpuUsage = cpuUsage
#        self.memoryUsage = memoryUsage
#        self.storageUsage = storageUsage
#        self.year = year
#        self.month = month
#        self.date = date
#        self.hour = hour


class VPSData:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value