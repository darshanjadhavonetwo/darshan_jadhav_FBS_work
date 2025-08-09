D = [2000, 500, 200, 100, 50, 20, 10, 5]
amt=int(input("enter the number:"))
for note in D:
    note_count = amt // note
    if note>0:
        print(f"{note} notes number is :{note_count}")
        amt%=note
if amt!=0:
    print(f"Remaining amount: {amt}")