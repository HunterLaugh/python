#coding:utf-8

# 转义字符 \
# \\ 斜线      \n 换行    \' '      \t tab键   
print("Let's practice everything.")
print("You \'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

#  字符串变量
poem="""
\t The lovely world with logic so firmly planted cannot discern \n the needs of love nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------------")
print(poem)
print("----------------")

# 计算
five=10-2+3-6
print("This is should be five: %s" % five)

# 函数定义
def secret_formula(started):
	jelly_beans=started*500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates   # 返回3个值

start_point=10000
beans,jars,crates=secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates))

start_point=start_point/10

print("We can alsodo that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))


