class Planner:
    def run(self, text):
        trace = []
        trace.append({'step':1,'action':'read_document'})
        return {
            'summary':'Draft discharge summary',
            'trace':trace
        }
