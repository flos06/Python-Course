# Write your solution here

def dict_of_numbers():
    dict = {}
    dict[0] = 'zero'
    till20 = ['one', 'two', 'three','four', 'five', 'six','seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    teens = ['twenty', 'thirty','forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    for num in range(1,20):
        dict[num] = till20[num - 1]
    teen = 0
    amount = 20
    for i in range(2, 10):
        
        for newnum in range(10):
            if newnum == 0:
                dict[amount] = teens[i - 2]
            else:

                dict[amount] = teens[teen] + '-' + till20[newnum - 1]
            amount += 1
        teen += 1

    return dict



