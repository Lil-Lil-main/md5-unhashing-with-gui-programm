from tkinter import Tk, Button, Label, Entry

from bruteforce import bruteforce


root = Tk()

# root settings 
root.resizable(False, False)
root.geometry('350x170')
root.title('BruteForce (md5)')
root['bg'] = 'purple'

def bruteforce_start():
	if other_dict_field.get() != '':
		try:
			user_hash = hash_entry_field.get()
			if user_hash != '':
				answer_word['text'] = bruteforce(user_hash, other_dict_field.get())
			else:
				answer_word['text'] = "Hash couldn't be empty"
		except FileNotFoundError:
			answer_word['text'] = 'Dictonary not found' 
	else:
		answer_word['text'] = 'Select dictonary'

# Title
name = Label(root, text='MD5 Brute', font='Arial 20', bg='purple', fg='white')

# Hash label
hash_label = Label(root, text='Enter hash:', font='Arial 15', bg='purple', fg='white')

# hash entry field
hash_entry_field = Entry(root, width=30)

# Other dict label
other_dict_label = Label(root, text='Enter directory:', font='Arial 13', bg='purple', fg='white')

# Other dict field
other_dict_field = Entry(root, width=30)

# Answer key label
answer_word_label = Label(root, text='Word:', font='Arial 15', bg='purple', fg='white')
answer_word = Label(root, text='', font='Arial 15', bg='purple', fg='white')

# BruteForce start button 
start_button = Button(
						root, 
						text='Start!', 
						width='25', 
						height='1', 
						bd=4, 
						font="Arial 14", 
						bg='darkred', 
						activebackground='black', 
						activeforeground='white',
						command=bruteforce_start
						)


# Title marking
name.place(x=105)

# Hash label marking
hash_label.place(x=10, y=40)
hash_entry_field.place(x=135, y=45)

# Dictonary marking
other_dict_label.place(x=10, y=70)
other_dict_field.place(x=135, y=75)

# Answer word marking
answer_word_label.place(x=10, y=100)
answer_word.place(x=135, y=100)

# BruteForce button marking
start_button.place(x=30, y=128)


# run programm
if __name__ == '__main__':
	root.mainloop()
