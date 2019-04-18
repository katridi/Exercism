class HighScores(object):

    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[-1]
        
    def personal_best(self):
        return max(self.scores)
        
    def personal_top_three(self):
        a = []
        scores = self.scores.copy()
        while scores:
            a.append(scores.pop(scores.index(max(scores))))
        return a[:3]
