import xml.etree.ElementTree as ET

# The following method are used to calculate the cost of operation on trees
# these method will take into consideration only Tags
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes
#   - InsTree = 1 if subtree available in A, else sum of nodes
#   - UpdTag = 1 if tags are diffent, 0 if same


def isTreeIdentical_Tag(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    if root1.tag != root2.tag:
        return False
    if len(root1) != len(root2):
        return False
    for i in range(0, len(root1)):
        if not isTreeIdentical_Tag(root1[i], root2[i]):
            return False
    return True


def isSubTree_Tag(root1, root2):
    # print(root1, root2)
    if root1 is None:
        return True

    if root2 is None:
        return False

    if isTreeIdentical_Tag(root1, root2):
        return True

    for i in range(0, len(root2)):
        if isSubTree_Tag(root1, root2[i]):
            return True

    return False


def findSubTree_Tag(root, subTreeName):
    subTreeRoot = root

    if len(subTreeName) > 1:
        indices = subTreeName[2 : len(subTreeName)].split("-")
        for index in indices:
            subTreeRoot = subTreeRoot[int(index)]

    return subTreeRoot


def nodeCounter_Tag(root):
    counter = 0

    if root is None:
        return counter

    counter += 1
    for child in root:
        counter += nodeCounter_Tag(child)

    return counter


def costInsert_Tag(subTreeB, A):
    if isSubTree_Tag(subTreeB, A):
        return 1
    else:
        return nodeCounter_Tag(subTreeB)


def costDelete_Tag(subTreeA, B):
    if isSubTree_Tag(subTreeA, B):
        return 1
    else:
        return nodeCounter_Tag(subTreeA)


def costUpd_Tag(rootA, rootB):
    if rootA.tag == rootB.tag:
        return 0
    else:
        return 1


# The following method are used to calculate the cost of operation on trees
# these method will take into consideration only Tags and text
# the cost model for it is:
#   - DelTree = 1 if subtree available in B, else sum of nodes + words
#   - InsTree = 1 if subtree available in A, else sum of nodes + words
#   - UpdTag = 1 if tags are diffent, 0 if same + cost of upd text


# def isTreeIdentical(root1, root2):
#     if root1 == None and root2 == None:
#         return True
#     if root1 == None or root2 == None:
#         return False
#     if root1.tag != root2.tag:
#         return False
#     if len(root1) != len(root2):
#         return False
#     for i in range(0, len(root1)):
#         if not isTreeIdentical(root1[i], root2[i]):
#             return False
#     return True


# def isSubTree(root1, root2):
#     # print(root1, root2)
#     if root1 is None:
#         return True

#     if root2 is None:
#         return False

#     if isTreeIdentical(root1, root2):
#         return True

#     for i in range(0, len(root2)):
#         if isSubTree(root1, root2[i]):
#             return True

#     return False


# def findSubTree(root, subTreeName):
#     subTreeRoot = root

#     if len(subTreeName) > 1:
#         indices = subTreeName[2 : len(subTreeName)].split("-")
#         for index in indices:
#             subTreeRoot = subTreeRoot[int(index)]

#     return subTreeRoot


# def nodeCounter(root):
#     counter = 0

#     if root is None:
#         return counter

#     counter += 1
#     for child in root:
#         counter += nodeCounter(child)

#     return counter


# def costInsert(subTreeB, A):
#     if isSubTree(subTreeB, A):
#         return 1
#     else:
#         return nodeCounter(subTreeB)


# def costDelete(subTreeA, B):
#     if isSubTree(subTreeA, B):
#         return 1
#     else:
#         return nodeCounter(subTreeA)


# def costUpd(elA, elB):
#     if elA.tag == elB.tag:
#         return 0
#     else:
#         return 1
