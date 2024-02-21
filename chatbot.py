from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello! I'm your HR support chatbot. How can I assist you today?"]
    ],
    
    [
        r"(.*)vacation(.*)",
        ["We offer 2 Vacation leaves for a period of 1 week. The 2 leaves can be redeemed within a gap of 4 months.\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)sick(.*)",
        ["We offer a total of 10 days of sick leave in an year.\nWhat else do you want to enquire?"]
    ],
    
    [
        r"(.*)paternity(.*)",
        ["We offer a paternity leave of 15 days.\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)maternity(.*)",
        ["We offer a maternity leave of 2 months.\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)parental(.*)",
        ["We offer the following Parental leaves:\n1) Maternity Leave\n2) Paternity Leave\nWhat do you want to know about?"]
    ],
    [
        r"(.*)leave(.*)",
        ["Of course! Our leave policy allows for:\n1) Vacation Leave \n2) Sick Leave \n3) Parental Leave \nWhat do you want to enquire about?"]
    ],
    [  r"(.*)fitness(.*)",
        ["We offer the following things to ensure your fitness: \n1) GYM reimbursement\n2) Health programmes \n3) Health insurance \nWhat do you want to enquire from this?"]
    ],
    [
        r"(.*)health(.*)",
        ["Our Health insurance covers: \n1) Dental Care\n2) Vision Care \n3) Mental health care.\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)benefits(.*)",
        ["We offer a the following Benefits and Insurances: \n1) Health insurances \n2) Paid vacation leaves \n3) Paid sick leaves\n4) Paid paretal leaves\n5) Purchasing perks\n6) Fitness \nWhat do you want to enquire from this?"]
    ],
    [
        r"(.*)Insurance(.*)",
        ["We offer a the following Benefits and Insurances: \n1) Health insurances \n2) Paid vacation leaves \n3) Paid sick leaves\n4) Paid paretal leaves\n5) Purchasing perks\n6) Fitness \nWhat do you want to enquire from this?"]
    ],
    
    [
        r"(.*)purchasing(.*)",
        ["We offer a reimbursement on products, programmes and courses which help you grow. There is a certain limit upto which we provide reimburesement. Please contact your HR to know more about it.\nWhat else do you want to enquire?"]
    ],
    
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello! I'm your HR support chatbot. How can I assist you today?"]
    ],
    
    
    [
        r"(.*)rent(.*)",
        ["The criteria for HRA is: Actual rent paid - 10% of your Basic pay"]
    ],
    [
        r"(.*)basic(.*)",
        ["Please contact your HR for this."]
    ],
    [
        r"(.*)bonus(.*)",
        ["Your bonus amount will be alloted on the basis of some parameters by your HR "]
    ],
    [
        r"(.*)house(.*)",
        ["The criteria for HRA is: Actual rent paid - 10 percent of your Basic pay"]
    ],
    [
        r"(.*)pay(.*)",
        ["Our Compensation structure is as follows:\n1) Basic Pay\n2) House Rent Allowance\n3) Bonus\n4) Benefits and Insurance\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)compensation(.*)",
        ["Our Compensation structure is as follows:\n1) Basic Pay\n2) House Rent Allowance\n3) Bonus\n4) Benefits and Insurance\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)contact(.*)",
        ["HR's contact information:\nGmail id : singhaldivyansh232@gmail.com \nMobile No. : 8887217242.\nWhat else do you want to enquire?"]
    ],
    [
        r"(.*)hr(.*)",
        ["HR's contact information:\nGmail id : singhaldivyansh232@gmail.com \nMobile No. : 8887217242.\nWhat else do you want to enquire?"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["I can assist you with the following options: \n1) Leave policy\n2) Benefits and Insurances\n3) Compensation structure \n4) HR contact information \nWhat do you want to enquire?"]
    ],
    
    
]

chat = Chat(pairs, reflections)
chat.converse()