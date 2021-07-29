
class DataTool:
    def __init__(self, st):
        self.st = st

    def data_tool(self):
        self.st.title('数据处理工具')

        self.st.header("比较两个数据的差集和并集")

        labelA = '请输入A的内容'

        a = self.st.text_area(labelA, value='', key=None).split("\n")

        labelB = '请输入B的内容'

        b = self.st.text_area(labelB, value='', key=None).split("\n")

        if len(a) > 1 and len(b) > 1:
            aDb = "\n".join(list(set(a).difference(set(b))))

            labelAdB = 'a多余b的内容'

            self.st.text_area(labelAdB, value=aDb, key=None)

            bDa = "\n".join(list(set(b).difference(set(a))))

            labelBdA = 'b多余a的内容'

            self.st.text_area(labelBdA, value=bDa, key=None)

            bAa = "\n".join(list(set(a).union(set(b))))

            labelBaA = 'a和b的并集'

            self.st.text_area(labelBaA, value=bAa, key=None)

            bCc = "\n".join(list(set(a).intersection(set(b))))

            labelBaC = 'a和b的交集'

            self.st.text_area(labelBaC, value=bCc, key=None)

        # ===================================================================================
        self.st.header("数组去重")

        labelE = '请输入数组的内容'

        e = self.st.text_area(labelE, value='', key=None).split("\n")

        f = "\n".join(list(set(e)))

        labelG = '数组去重后的结果'

        self.st.text_area(labelG, value=f, key=None)

        # ===================================================================================
        self.st.header("JSON转换")

        labelG = "json转换"

        g = self.st.text_area(labelG, value='', key=None)

        if g:
            self.st.write("json转换结果")

            self.st.json(g)

        # ===================================================================================
        self.st.header("比较第一个数组是否包含在第二个数组中某个字符串")

        labelZ = '请输入A的内容'

        z = self.st.text_area(labelZ, key=False).split("\n")

        labelV = '请输入B的内容'

        v = self.st.text_area(labelV, key=False).split("\n")

        o = []
        for zz in z:
            for vv in v:
                if len(vv.split(",")) > 1:
                    if vv.split(",")[0] != '' and zz != '':
                        if vv.split(",")[1] in zz and vv.split(",")[0] != zz:
                            o.append(zz + ',' + vv.split(",")[0])

        q = '结果集'
        o = "\n".join(o)
        if len(o) > 0:
            self.st.text_area(q, value=o, key=None)
