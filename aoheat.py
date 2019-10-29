#This program takes the average temperature and gives back the total number of
#cooling and heating degree days
#By Arturo Ortiz, arturo.ortiz1@marist.edu

def main():
    temp= input("Enter the average tempurature per day separated by spaces: ")
    temp=temp.split(" ")
    cooling=0
    heating=0

    for i in temp:
        if float(i)> 80 or float(i)<60:
            if float(i)> 80:
                cooling += float(i)-80
            else:
                heating += 60-float(i)

        print("There are", cooling, "cooling degrees days and there are ", heating, "heating degrees days")
main()
