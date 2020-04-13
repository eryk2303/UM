import Test
import Print_tree

def main():
    x = 1
    while x is not 0:
        print("Wybierz opcje:")
        print("Wykonaj gotowe testy - 1")
        print("wykonaj swoje testy - 2")
        print("WWyjdz - 0")
        x = input()
        if x is "1":
            print("pierwsze drzewo")
            tree1 = Test.third_test(0.5, 0.25, 0.25)
            print("drugie drzewo")
            tree2 = Test.third_test(0.25, 0.25, 0.50)
            print("trzecie drzewo")
            tree3 = Test.third_test(0.05, 0.85, 0.1)
            print("Wypisz drzewo")
            y = input()
            print('podaj numer dzrewa')
            if y is '1':
                Print_tree.print_tree(tree1, "")
            elif y is '2':
                Print_tree.print_tree(tree2, "")
            elif y is '3':
                Print_tree.print_tree(tree3, "")
            else:
                continue
        elif x is '2':
            print("podaj ile razy chcesz doszkalać drzewo (max 3): ")
            t = input()
            if t is '0':
                print("podaj procent ilości danych którą chcesz nauczyć drzewo")
                v = float(input())
                tree = Test.first_test(v)


        
main()
