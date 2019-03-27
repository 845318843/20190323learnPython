# # my_file = open('my_filename.txt', 'r')
# #
# # # my_file = open('notes.txt', 'r')
# # #
# # #
# # # line = my_file.readline()
# # # lines = my_file.readlines()
# # #
# # # my_file.close()
# # # print(lines)
# # # print(line)
# #
# # # # 22-2
# # # my_file = open('notes.txt', 'r')
# # # first_line = my_file.readline()
# # # # my_file.seek(0)
# # # second_line = my_file.readline()
# # # print("firstline:",first_line)
# # # print("secondline", second_line)
# # # my_file.close()
# # #
# # # # my_file = open('new_notes.txt','r')
# # # # my_file = open('new_notes.txt', 'w')
# # # # my_file = open('notes.txt', 'a')
# # #
# # #
# # # todo_list = open('notes.txt', 'a')
# # # todo_list.write('\nSpend allowance')
# # # todo_list.close()
# # #
# # # new_file = open("my_new_notes.txt", 'w')
# # # new_file.write("Eat supper\n")
# # # new_file.write("Play soccer\n")
# # # new_file.write("Go to bed")
# # # new_file.close()
# # #
# # #
# # # the_file = open('notes.txt', 'w')
# # # the_file.write("Wake up\n")
# # # the_file.write("Watch cartoons")
# # # the_file.close()
# # #
# # # my_file = open("new_file.txt", 'w')
# # # # print(my_file, "Hello there, neighbor!")  python3 中不能工作
# # # my_file.close()
# #
# #
# #
# #
# #
# # import pickle
# # my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
# # pickle_file = open('my_pickled_list.pkl','w')
# # pickle.dump(my_list, pickle_file)# python3 up against wrong
# # pickle_file.close()
# #
# #
# # pickle_file = open('my_pickled_list.pkl', 'r')
# # recovered_list = pickle.load(pickle_file)
# # pickle_file.close()
# # print(recovered_list)

# what did you learn?
# open("filename.xxx",r)
# myfile.close()


# test items
#1. 称为 文件对象
#2. open("filename",'r')
#3. 文件对象是操作文件的工具
#4. open和 close
#5. 文件尾部追加
#6. 原内容丢失
#7. seek(0)
#8. pickle.dump（）
#9. pickle.load()


