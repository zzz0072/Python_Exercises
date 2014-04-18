#/usr/bin/env python
import package_test.module1.my_sum
import package_test.module2.my_print

print (dir())
print(package_test.module1.my_sum.my_sum("I am ", "zzz"))
package_test.module2.my_print.my_print("I am zzz1")
