根据中序遍历(inorder)及前序遍历(preorder)的2个数组数据，创建出原始二叉树对象
1）根据前序遍历数组，找到root节点。
2）根据root节点找到其在中序遍历数组中的index（记为im），所有左边的数据是左子树，所有右边的数据是右子树。
3）写一个函数，参数为2个数组及各自的开始-结束的index(闭区间)，然后递归调用，重复上述步骤1和2。
要点记录：因为2个数组大小相同，且每个左右子树的结点数目也相同，因此有一个关键公式
im-ibegin=pm-pbegin,
其中ibegin和iend是inorder数组的开始和结束坐标，pbegin和pend为preorder数组的开始和结束左边。pm为前序遍历数组中左子树的分界点。
TreeNode left = buildTree(preorder, inorder, pbegin + 1, pm, ibegin, im - 1);
TreeNode right = buildTree(preorder, inorder, pm + 1, pend, im + 1, iend);
注意：左子树的开始坐标要过滤掉当前root即从pbegin+1开始。

当前序数组改成后序遍历(postorder)数组时，原理类似。
TreeNode left = buildTree(preorder, inorder, pbegin, pm-1, ibegin, im - 1);
TreeNode right = buildTree(preorder, inorder, pm, pend-1, im + 1, iend);
注意：pm和pend都要减1，因为root是pend。

口诀：边界，前序前加1，后序后减1。

如果只给提供前序和后序，则不能直接找到m，需要根据preorder的左子树root节点开始找，这样找到左子树和右子树的分界点。
