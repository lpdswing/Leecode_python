class Node(object):

    def __init__(self, data):
        self.data = data  # 节点的数据
        self.next_node = None  # 节点的下一节点

    # def set_next_node(self, node):
    #   self.next_node = node

    def __repr__(self):
        return self.data  # 格式化输出


class LinkedList(object):

    def __init__(self):

        self.head = None  # 链表的头节点
        self.num = None  # 链表的长度

    def append(self, data):
        """在尾部添加一个节点"""
        p = self.getitem(self.num - 1)  # 获取尾部的节点
        p.next_node = Node(data)  # 给尾部节点的下一节点赋值
        self.num += 1  # 总长增加1

    def remove(self, index):
        """移除链表中的某一个节点"""

        if index.isdigit() and int(index) in range(self.num):  # 如果index全是数字并且在0，到总长度减一的范围中
            p = self.getitem(int(index))  # 获取当前节点
            if p is not self.head:  # 如果当前节点不是头节点
                p_pre = self.getitem(int(index) - 1)  # 获取上一个节点
                p_pre.next_node = p.next_node  # 上一节点的下一节点变为要删除节点的下一节点
            else:
                self.head = p.next_node  # 当前节点是头节点则， 头节点变为下一个节点
            self.num -= 1  # 长度减一

        elif not index.isdigit():
            node = self.head
            pre_node = None  # 记录前一个节点
            for i in range(self.num):
                if index == node.data:  # 如果index和某个数据的节点数据一样
                    if pre_node == None:  # 如果没有前一个节点，就为头节点
                        self.head = node.next_node  # 头节点等于原头节点的下一节点
                    else:
                        pre_node.next_node = node.next_node  # 前一节点的下一个节点等于想要删除的当前节点的下一节点
                    self.num -= 1
                node, pre_node = node.next_node, node
        else:
            print('链表中不存在的对象！')

    def insert(self, data, index):
        """在链表中的某个位置插入一个节点"""

        current_p = self.getitem(index)  # 获取想要插入位置节点
        node = Node(data)  # 创建新节点
        if index == 0:  # 在头节点前插入一条数据
            node.next_node, self.head = self.head, node
            self.num += 1
        else:
            if index == self.num - 1:  # 表示想要在最后一个位置插入一个节点
                current_p.next_node = node
                self.num += 1
            elif index < self.num - 1:
                next_node = self.getitem(index + 1)  # 获取想要插入位置的下一节点
                current_p.next_node = node
                node.next_node = next_node  # 获取下一个节点
                self.num += 1
            else:
                print('链表中不存在的对象!')

    def change(self, data, index):
        """改变某一节点的数据"""

        current_p = self.getitem(index)  # 获取当前节点
        current_p.data = data  # 修改

    def init_link(self, data):
        """创建一个新的链表"""

        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next_node = node
            p = node
        self.num = self.size()

    def getitem(self, index):
        """获取某一个位置的节点"""

        p = self.head
        for i in range(index):
            p = p.next_node

        return p

    def size(self):
        """获取当前链表的长度"""

        p = self.head
        index = 1
        while p.next_node:  # 如果当前节点还有下一个节点的地址, 则表示后面还存在节点, 如果为空，则没有了
            index += 1
            p = p.next_node
        return index

    def all_node(self):
        """获取链表中的所有数据"""

        for i in range(self.num):
            print('%s: %s' % (i + 1, self.getitem(i)))


def menu():
    """菜单显示"""
    print()
    print('-------------------------------------------------------')
    print('*****************欢迎使用学生查询系统********************')
    print('******************1. 查看学生总人数*********************')
    print('******************2. 查看所有学生  *********************')
    print('******************3. 尾部添加学生  *********************')
    print('******************4. 插入一个学生  *********************')
    print('******************5. 删除一个学生  *********************')
    print('******************6. 查看某个学生  *********************')
    print('******************7. 修改学生名字  *********************')
    print('******************8. 退出本系统    *********************')
    print('-------------------------------------------------------')
    print()


def switch_choose(link, num):
    """选择操作方法"""
    if num == 1:
        print('学生共有%s个' % link.size())

    if num == 2:
        link.all_node()

    if num == 3:
        name = input('请输入学生名字：')
        link.append(name)

    if num == 4:
        name = input('请输入学生名字：')
        index = int(input('请输入要插入的位置:'))
        link.insert(name, index)

    if num == 5:
        index_or_name = input('请输入想要移除的学生的位置或者名字：')
        link.remove(index_or_name)

    if num == 6:
        index = int(input('请输入想要查看学生的位置：'))
        print(link.getitem(index))

    if num == 7:
        name = input('请输入学生名字：')
        index = int(input('请输入要改变的学生的位置:'))
        link.change(name, index)


def main(data):
    link = LinkedList()  # 构造一个对象
    link.init_link(data)  # 创建一个新的链表

    while True:
        menu()
        choose = int(input('请选择操作选项：'))

        if choose == 8:
            break
        switch_choose(link, choose)


if __name__ == '__main__':
    student_list = ['张三', '李四', '王五']
    main(student_list)
