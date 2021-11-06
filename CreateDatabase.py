import pandas as pd
import numpy as np
dataset1={'Items':['Digital Camera','Lab Top','Desk Top','Printer','Flash Drive',
             'Microsoft Office','Speakers','Lab Top Case','Anti-Virus','External Hard-Drive']}
BestBuy_dataItems=pd.DataFrame(dataset1, index=[1,2,3,4,5,6,7,8,9,10])
#print(Amazon_dataItems)

dataset2={'Items':['Quilts','Bedspreads','Decorative Pillows','Bed Skirts','Sheets','Shams','Bedding Collections',
                   'Kids Bedding','Embroidered Bedspread','Towels']}
kmart_dataItems=pd.DataFrame(dataset2,index=[1,2,3,4,5,6,7,8,9,10])
#print(kmart_dataItems)

dataset3={'Items':['Running Shoe','Soccer Shoe','Socks','Swimming Shirt','Dry Fit V-Nick','Rash Guard','Sweatshirts',
                   'Hoodies','Tech Pants','Modern Pants']}
Nike_dataItems=pd.DataFrame(dataset3,index=[1,2,3,4,5,6,7,8,9,10])
#print(Nike_dataItems)

dataset4={'Items':['A Beginner Guide','Java:The Complete Reference','Java For Dummies',
                   'Android Programming:The Big Nerd Ranch','Head First Java 2nd Edition','Beginning Programming with Java',
                   'Java 8 Pocket Guide','C++ Programming in Easy Steps','Effective Java (2nd Edition)',
                   'HTML and CSS: Design and Build Websites']}
Amazon_dataItems=pd.DataFrame(dataset4,index=[1,2,3,4,5,6,7,8,9,10])
#print(Amazon_dataItems)

dataset5={'Items':['Milk','Pear','Apple','Muffins','Green vegetables','Dishwasher gel','Chocolates','Banana','Meat','Cornflakes']}
Supremo_dataItems=pd.DataFrame(dataset5,index=[1,2,3,4,5,6,7,8,9,10])
#print(Supremo_dataItems)


data1 = {'Transaction': [['Desk Top', 'Printer', 'Flash Drive', 'Microsoft Office', 'Speakers', 'Anti-Virus'],
                        ['Lab Top', 'Flash Drive', 'Microsoft Office', 'Lab Top Case', 'Anti-Virus'],
                        ['Lab Top', 'Printer', 'Flash Drive', 'Microsoft Office', 'Anti-Virus', 'Lab Top Case', 'External Hard-Drive'],
                        ['Lab Top', 'Printer', 'Flash Drive', 'Anti-Virus', 'External Hard-Drive', 'Lab Top Case'],
                        ['Lab Top', 'Flash Drive', 'Lab Top Case', 'Anti-Virus'],
                        ['Lab Top', 'Printer', 'Flash Drive', 'Microsoft Office'],
                        ['Desk Top', 'Printer', 'Flash Drive', 'Microsoft Office'],
                        ['Lab Top', 'External Hard-Drive', 'Anti-Virus'],
                        ['Desk Top', 'Printer', 'Flash Drive', 'Microsoft Office', 'Lab Top Case', 'Anti-Virus', 'Speakers', 'External Hard-Drive'],
                        ['Digital Camera' , 'Lab Top', 'Desk Top', 'Printer', 'Flash Drive', 'Microsoft Office', 'Lab Top Case', 'Anti-Virus', 'External Hard-Drive', 'Speakers'],
                        ['Lab Top', 'Desk Top', 'Lab Top Case', 'External Hard-Drive', 'Speakers', 'Anti-Virus'],
                        ['Digital Camera' , 'Lab Top', 'Lab Top Case', 'External Hard-Drive', 'Anti-Virus', 'Speakers'],
                        ['Digital Camera' , 'Speakers'],
                        ['Digital Camera' , 'Desk Top', 'Printer', 'Flash Drive', 'Microsoft Office'],
                        ['Printer','Flash Drive', 'Microsoft Office', 'Anti-Virus', 'Lab Top Case', 'Speakers', 'External Hard-Drive'],
                        ['Digital Camera', 'Flash Drive', 'Microsoft Office', 'Anti-Virus', 'Lab Top Case', 'External Hard-Drive', 'Speakers'],
                        ['Digital Camera' , 'Lab Top', 'Lab Top Case'],
                        ['Digital Camera' , 'Lab Top Case', 'Speakers'],
                        ['Digital Camera' , 'Lab Top', 'Printer', 'Flash Drive', 'Microsoft Office', 'Speakers', 'Lab Top Case', 'Anti-Virus'],
                        ['Digital Camera' , 'Lab Top', 'Speakers', 'Anti-Virus', 'Lab Top Case']
    ]
       }


DB1 = pd.DataFrame(data1,index=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'])
DB1.to_excel('BestBuy.xlsx')

data2 = {'Transaction': [['Decorative Pillows', 'Quilts', 'Embroidered Bedspread'],
                        ['Embroidered Bedspread', 'Shams', 'Kids Bedding', 'Bedding Collections', 'Bed Skirts', 'Bedspreads', 'Sheets'],
                        ['Decorative Pillows', 'Quilts', 'Embroidered Bedspread', 'Shams', 'Kids Bedding', 'Bedding Collections'],
                        ['Kids Bedding', 'Bedding Collections', 'Sheets', 'Bedspreads', 'Bed Skirts'],
                        ['Decorative Pillows', 'Kids Bedding', 'Bedding Collections', 'Sheets', 'Bed Skirts', 'Bedspreads'],
                        ['Bedding Collections', 'Bedspreads', 'Bed Skirts', 'Sheets', 'Shams', 'Kids Bedding'],
                        ['Decorative Pillows', 'Quilts'],
                        ['Decorative Pillows', 'Quilts','Embroidered Bedspread'],
                        ['Bedspreads', 'Bed Skirts', 'Shams', 'Kids Bedding', 'Sheets'],
                        ['Quilts', 'Embroidered Bedspread', 'Bedding Collections'],
                        ['Bedding Collections', 'Bedspreads', 'Bed Skirts', 'Kids Bedding', 'Shams', 'Sheets'],
                        ['Decorative Pillows', 'Quilts'],
                        ['Embroidered Bedspread', 'Shams'],
                        ['Sheets', 'Shams', 'Bed Skirts', 'Kids Bedding'],
                        ['Decorative Pillows', 'Quilts'],
                        ['Decorative Pillows', 'Kids Bedding', 'Bed Skirts', 'Shams'],
                        ['Decorative Pillows', 'Shams', 'Bed Skirts'],
                        ['Quilts', 'Sheets', 'Kids Bedding'],
                        ['Shams', 'Bed Skirts', 'Kids Bedding', 'Sheets'],
                        ['Decorative Pillows', 'Bedspreads', 'Shams', 'Sheets', 'Bed Skirts', 'Kids Bedding']]
       }


DB2 = pd.DataFrame(data2,index=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'])
DB2.to_excel('kmart.xlsx')

data3 = {'Transaction': [['Running Shoe', 'Socks', 'Sweatshirts', 'Modern Pants'],
                    ['Running Shoe', 'Socks', 'Sweatshirts'],
                    ['Running Shoe', 'Socks', 'Sweatshirts', 'Modern Pants'],
                    ['Running Shoe', 'Sweatshirts', 'Modern Pants'],
                    ['Running Shoe', 'Socks', 'Sweatshirts', 'Modern Pants', 'Soccer Shoe'],
                    ['Running Shoe', 'Socks', 'Sweatshirts'],
                    ['Running Shoe', 'Socks', 'Sweatshirts', 'Modern Pants', 'Tech Pants', 'Rash Guard', 'Hoodies'],
                    ['Swimming Shirt', 'Socks', 'Sweatshirts'],
                    ['Swimming Shirt', 'Rash Guard', 'Dry Fit V-Nick', 'Hoodies', 'Tech Pants'],
                    ['Swimming Shirt', 'Rash Guard', 'Dry Fit V-Nick'],
                    ['Swimming Shirt', 'Rash Guard', 'Dry Fit V-Nick'],
                    ['Running Shoe', 'Swimming Shirt', 'Socks', 'Sweatshirts', 'Modern Pants', 'Soccer Shoe', 'Rash Guard', 'Hoodies', 'Tech Pants', 'Dry Fit V-Nick'],
                    ['Running Shoe', 'Swimming Shirt', 'Socks', 'Sweatshirts', 'Modern Pants', 'Soccer Shoe', 'Rash Guard', 'Tech Pants', 'Dry Fit V-Nick', 'Hoodies'],
                    ['Running Shoe', 'Swimming Shirt', 'Rash Guard', 'Tech Pants', 'Hoodies', 'Dry Fit V-Nick'],
                    ['Running Shoe', 'Swimming Shirt', 'Socks', 'Sweatshirts', 'Modern Pants', 'Dry Fit V-Nick', 'Rash Guard', 'Tech Pants'],
                    ['Swimming Shirt', 'Soccer Shoe', 'Hoodies', 'Dry Fit V-Nick', 'Tech Pants', 'Rash Guard'],
                    ['Running Shoe', 'Socks'],
                    ['Socks', 'Sweatshirts', 'Modern Pants', 'Soccer Shoe', 'Hoodies', 'Rash Guard', 'Tech Pants', 'Dry Fit V-Nick'],
                    ['Running Shoe', 'Swimming Shirt', 'Rash Guard'],
                    ['Running Shoe', 'Swimming Shirt', 'Socks', 'Sweatshirts', 'Modern Pants', 'Soccer Shoe', 'Hoodies', 'Tech Pants', 'Rash Guard', 'Dry Fit V-Nick']]
       }


DB3 = pd.DataFrame(data3,index=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'])
DB3.to_excel('Nike.xlsx')

data4 = {'Transaction':[['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition'],
                        ['Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition' , 'Beginning Programming with Java'],
                        ['Android Programming: The Big Nerd Ranch', 'Beginning Programming with Java', 'Java 8 Pocket Guide'],
                        ['A Beginner Guide', 'Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition'],
                        ['A Beginner Guide', 'Head First Java 2nd Edition' , 'Beginning Programming with Java'],
                        ['Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['Java For Dummies', 'Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition' , 'Beginning Programming with Java'],
                        ['Beginning Programming with Java', 'Java 8 Pocket Guide', 'C++ Programming in Easy Steps'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'HTML and CSS: Design and Build Websites'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Java 8 Pocket Guide', 'HTML and CSS: Design and Build Websites'],
                        ['Java For Dummies', 'Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition'],
                        ['Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies', 'Android Programming: The Big Nerd Ranch'],
                        ['Head First Java 2nd Edition' , 'Beginning Programming with Java', 'Java 8 Pocket Guide'],
                        ['Android Programming: The Big Nerd Ranch', 'Head First Java 2nd Edition'],
                        ['A Beginner Guide', 'Java: The Complete Reference', 'Java For Dummies']]
       }


DB4 = pd.DataFrame(data4,index=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'])
DB4.to_excel('Amazon.xlsx')


data5 = {'Transaction':[['Milk','Banana', 'Pear', 'Apple', 'Muffins'],
                        ['Meat', 'Pear', 'Apple'],
                        ['Milk', 'Pear', 'Apple', 'Muffins', 'Green Vegetables'],
                        ['Muffins', 'Green Vegetables' , 'Dishwasher Gel'],
                        ['Muffins', 'Dishwasher Gel','Meat', 'Chocolates','Banana'],
                        ['Milk', 'Muffins', 'Green Vegetables'],
                        ['Milk', 'Green Vegetables' , 'Dishwasher Gel','Banana'],
                        ['Pear', 'Apple', 'Muffins'],
                        ['Apple', 'Muffins', 'Green Vegetables' ,'Cornflakes', 'Dishwasher Gel'],
                        ['Dishwasher Gel', 'Chocolates', 'Banana'],
                        ['Milk', 'Pear', 'Apple', 'Muffins'],
                        ['Milk', 'Pear', 'Apple', 'Meat','Cornflakes'],
                        ['Milk', 'Pear', 'Apple', 'Chocolates', 'Meat'],
                        ['Apple', 'Muffins', 'Green Vegetables'],
                        ['Apple','Banana', 'Muffins'],
                        ['Milk', 'Pear', 'Meat', 'Muffins','Banana'],
                        ['Milk', 'Pear', 'Apple', 'Muffins'],
                        ['Green Vegetables' , 'Dishwasher Gel', 'Chocolates'],
                        ['Muffins', 'Green Vegetables','Meat'],
                        ['Milk', 'Pear', 'Apple','Cornflakes']]
       }


DB5 = pd.DataFrame(data5,index=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20'])
DB5.to_excel('Supremo.xlsx')

