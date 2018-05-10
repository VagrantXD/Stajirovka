#!/bin/python3

#In the Deca Forest, grow the Deca Trees.
#
#On each Deca Tree, a trunk has 10 branches.
#
#On each branch, there are 10 twigs.
#
#On each twig, there are 10 leaves.
#
#Unfortunately, the Deca Forest is becoming wildly overgrown and is endangering the local wildlife. You must add methods to the tree object so that the woodcutter can remove parts of a tree as follows, where n is a positive integer:
#
#chop_trunk(n)     will remove n trunks
#chop_branch(n)    will remove n branches
#chop_twig(n)      will remove n twigs
#chop_leaf(n)      will remove n leaves
#Make sure that when you remove any part of the tree, you also remove all the smaller parts attached to it. e.g. if you remove a twig you must also remove 10 leaves from the tree object. The woodcutter's aim is to trim back this forest, so he will try to remove as much of the tree as possible each time he chops.
#
#Conversely, when you remove a smaller part, you do not need to remove the larger parts it is attached to - for example you could pick off all the leaves from a tree and the number of twigs, branches and trunks would be unaffected.
#
#The tree cannot have a negative number of trunks, branches, leaves or twigs. That would be highly unnatural.
#
#You must also add a method 'describe' that allows the Deca Forest tourguides to describe each tree. It should describe the tree in the following format:
#
#"This tree has a trunks, b branches, c twigs and d leaves."
#
#(where a, b, c and d are integer values)
#
#Your methods will be tested for trees with varying numbers of trunks and for removing random numbers of leaves, twigs, branches and trunks. The test will use only positive integers for these values.
#
#For more information on JS objects, take a look here


class Tree:
    def __init__(self, trunks):
        self.trunks = trunks
        self.branches = trunks * 10
        self.twigs = trunks * 100
        self.leaves = trunks * 1000
    
    def chop_trunk( self, n ) :
        self.trunks = self.trunks - n if self.trunks - n > 0 else 0
        self.chop_branch( n * 10 )
        
    def chop_branch( self, n ) :
        self.branches = self.branches - n if self.branches - n > 0 else 0 
        self.chop_twig( n * 10 )
        
    def chop_twig( self, n ) :
        self.twigs = self.twigs - n if self.twigs - n > 0 else 0 
        self.chop_leaf( n * 10 )
       
    def chop_leaf( self, n ) :
        self.leaves = self.leaves - n if self.leaves - n > 0 else 0 
        
    def describe( self ) :
        return "This tree has {} trunks, {} branches, {} twigs and {} leaves.".format( self.trunks, 
                self.branches, self.twigs, self.leaves ) 

if __name__ == "__main__" :
    myTree = Tree( 10 )
    myTree.chop_trunk( 7 )
    print( myTree.describe() )
    myTree.chop_twig( 60 )
    print( myTree.describe() )
    myTree.chop_branch( 10000 )
    print( myTree.describe() ) 
