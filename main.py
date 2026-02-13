
# We have a csv file with the following content:

# file_name,version,size_bytes,content_type 

# file1.txt,1,100,text/plain 

# file2.txt,1,200,text/plain 

# file3.txt,2,150,text/plain

# We want to parse this file/text_csv and create a dictionary object that we can use to look up information about files in the csv.

# Once function work we want to do the same with a class and class methods.

fi = open("file.txt", "r")



csv_text = """file_name: ,version: ,size_bytes: ,content_type: 
file1.txt ,1 ,100 ,text/plain  
file2.txt ,1 ,200 ,text/plain  
file3.txt ,2 ,150 ,text/plain 
"""


def listview(num):
    parsed_text = csv_text.split("\n")
    list = parsed_text[num].split(",")
    return list

def titles():
    parsed_text = csv_text.split("\n")
    title = parsed_text[0].split(",")
    return title

def list_view_external(path, num):
    parsed_text = path.split("\n")
    list = parsed_text[num].split(",")
    return list

r = list_view_external((fi.read()), 1)
print(r)

#def parse_csv_from_file(file_path):
    #pass

if __name__ == "__main__":

    print("Which list would you like to view?")
    viewlist = input("I would like to view list (1-3):")


    lister = listview(int(viewlist))
    title = titles()
    print(title[0]+lister[0]+title[1]+lister[1]+title[2]+lister[2]+title[3]+lister[3])
     # should print: {'version': '1', 'size_bytes': '100', 'content_type': 'text/plain'}