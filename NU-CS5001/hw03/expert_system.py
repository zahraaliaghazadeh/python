def aching_bones_or_joints():

    joints_ans = input("Do you have aching bones or aching joints? (y/n) :")
    # Joints pain conditions
    if(error_input(joints_ans) == "y"):
        print("Possibilities include viral infection")
    elif(error_input(joints_ans) == "n"):
        rash_ans = input("Do you have a rash? (y/n) :")
        # rash conditions
        if (error_input(rash_ans) == "y"):
            print("Insufficient information to list possibilities")
        elif (error_input(rash_ans) == "n"):
            sore_throat_ans = input("Do you have a sore throat? (y/n) :")
            # sore throat conditions
            if(error_input(sore_throat_ans) == "y"):
                print("Possibilities include a throat infection")
            elif(error_input(sore_throat_ans) == "n"):
                back_pain_ans = input("Do you have back pain just"
                                      "above the waist with chills"
                                      "and fever? (y/n) :")
                # back pain conditions
                if(error_input(back_pain_ans) == "y"):
                    print("Possibilities include kidney infection")
                elif(error_input(back_pain_ans) == "n"):
                    urinary_pain_ans = input("Do you have pain urinating"
                                             "or are urinating more often?"
                                             "(y/n) :")
                    # urinary pain conditions
                    if(error_input(urinary_pain_ans) == "y"):
                        print("""Possibilities include a urinary
                             tract infection.""")
                    elif(error_input(urinary_pain_ans) == "n"):
                        sun_ans = input("Have you spent the day in the sun"
                                        "or in hot condition? (y/n) :")
                        # sun exposure conditions
                        if(error_input(sun_ans) == "y"):
                            print("Possibilities sunstroke or heat"
                                  "exhaustion.")
                        elif(error_input(sun_ans) == "n"):
                            print("Insufficient information to"
                                  "list possibilities.")


# helper function for error handling of invalid input
def error_input(answer):
    # while loop for when answer is not y/n
    while (answer != "y" and answer != "n"):
        answer = input("Please only enter y or n: ")
    return answer


def main():

    # beginning of the diagram questions
    coughing = input("Are you coughing? (y/n) :")
    # coughing conditions
    if (error_input(coughing) == "y"):
        shortness_of_breath = input("Are you short of breath or wheezing or"
                                    "coughing up phlegm? (y/n) :")
        # shortness of breath conditions
        if(error_input(shortness_of_breath) == "y"):
            print("Possibilities include pneumonia or infection of airways")
        elif(error_input(shortness_of_breath) == "n"):
            headache_ans = input("Do you have a headache? (y/n) :")
            # headache conditions
            if(error_input(headache_ans) == "y"):
                print("possibilities include viral infection")
            elif(error_input(headache_ans) == "n"):
                aching_bones_or_joints()
    elif(error_input(coughing) == "n"):
        headache_prompt = input("Do you have a headache? (y/n) :")
        # headache conditions
        if(error_input(headache_prompt) == "y"):
            menigitis_symptoms = input("Are you experiencing any of the"
                                       " following:"
                                       "pain when bending your head forward,"
                                       "nausea or womiting, \n"
                                       "bright light hurting your eyes,"
                                       "drowsiness or confusion? (y/n) :")
            # menigitis conditions
            if(error_input(menigitis_symptoms) == "y"):
                print("Possibilities include menigitis.")
            elif(error_input(menigitis_symptoms) == "n"):
                vomiting_ans = input("Are you vomiting or had diarrhea?"
                                     "(y/n) :")
                # vomiting conditions
                if (error_input(vomiting_ans) == "y"):
                    print("Possibilities include digestive tract infection.")
                elif(error_input(vomiting_ans) == "n"):
                    aching_bones_or_joints()
        elif(error_input(headache_prompt == "n")):
            aching_bones_or_joints()


main()
