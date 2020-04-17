from converter.pipelines import ProcessValuespacePipeline;

class ValuespaceHelper:
    @staticmethod
    def mimetypeToLearningResourceType(mimetype):
        if mimetype.startswith('video/'):
            return 'video'
        if mimetype.startswith('image/'):
            return 'image'
        if mimetype.startswith('audio/'):
            return 'audio'
        return None

    # range must be an array [from, to]
    @staticmethod
    def educationalContextByAgeRange(range):
        context = []
        if int(range[0])<=4:
            context.append('Grundschule')
        if int(range[1])>=4 and int(range[0])<=10:
            context.append('Sekundarstufe 1')
        if int(range[0])>=11 or int(range[1])>=11:
            context.append('Sekundarstufe 2')
        if len(context):
            return context
        return None