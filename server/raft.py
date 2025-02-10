# File: server/raft.py  
class RaftNode:  
    def __init__(self):  
        self.current_term = 0  
        self.voted_for = None  
        self.log = []  
        self.state = 'follower'  # 'leader'/'candidate'/'follower'  

    def request_vote(self, candidate_term, candidate_id):  
        if candidate_term > self.current_term:  
            self.current_term = candidate_term  
            self.voted_for = candidate_id  
            return True  
        return False  

    def append_entries(self, term, leader_id, entries):  
        if term >= self.current_term:  
            self.current_term = term  
            self.log.extend(entries)  
            return True  
        return False  