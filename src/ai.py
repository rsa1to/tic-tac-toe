from game import Move, Game, USER_PLAYER, AI_PLAYER

MAX_DEPTH = 6

class Node:
    def __init__(self, state, player_type, prev_move=None, score=None):
        self.state = state
        self.children = []
        self.player_type = player_type
        self.prev_move = prev_move
        self.score = score
    
    def is_terminal(self):
        return len(self.children) == 0

class AI:
    def __init__(self, root_state, search_depth=MAX_DEPTH): 
        self.root = Node(root_state, AI_PLAYER)
        self.search_depth = search_depth
        self.simulator = Game()
        self.simulator.set_state(root_state)

    def build_tree(self, node = None, depth = 0):
        score = 0
        curr_state = self.simulator.current_state()

        if depth > MAX_DEPTH:
            return
        if (depth == 0):
            self.build_tree(self.root, depth+1)
        elif (depth % 2 == 1):
            positions = self.simulator.get_open_positions() 
            for pos in positions:
                curr_move = Move(pos[0], pos[1], label=AI_PLAYER)
                if self.simulator.is_valid_move(curr_move) == True:
                    self.simulator.make_move(curr_move)
                    if self.simulator.has_winner():
                        score = 10
                        new_node = Node(self.simulator.current_state(), USER_PLAYER, curr_move, score)
                        node.children.append(new_node)
                    else:
                        new_node = Node(self.simulator.current_state(), USER_PLAYER, curr_move, score)
                        self.build_tree(new_node, depth+1)
                        node.children.append(new_node)
                self.simulator.set_state(curr_state)
        else:
            positions = self.simulator.get_open_positions()
            for pos in positions:
                curr_move = Move(pos[0], pos[1], label=USER_PLAYER)
                if self.simulator.is_valid_move(curr_move) == True:
                    self.simulator.make_move(curr_move)
                    if self.simulator.has_winner():
                        score = -10
                        new_node = Node(self.simulator.current_state(), AI_PLAYER, curr_move, score)
                        node.children.append(new_node)
                    else:
                        new_node = Node(self.simulator.current_state(), AI_PLAYER, curr_move, score)
                        self.build_tree(new_node, depth+1)
                        node.children.append(new_node)
                self.simulator.set_state(curr_state)

    def minimax(self, node=None):
        if node.is_terminal() == True:
            return (None, node.score)
        
        if node.player_type == USER_PLAYER:
            scores = []
            for child_node in node.children:
                score = self.minimax(child_node)[1]
                scores.append((child_node.prev_move, score))
            min_tuple = min(scores, key=lambda x: x[1])
            return min_tuple
        
        if node.player_type == AI_PLAYER:
            scores = []
            for child_node in node.children:
                score = self.minimax(child_node)[1]
                scores.append((child_node.prev_move, score))
            max_tuple = max(scores, key=lambda x: x[1])
            return max_tuple
        
    def best_move(self):
        self.build_tree(self.root)
        move, _ = self.minimax(self.root)
        return move