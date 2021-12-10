def countingValleys(steps, path):
    # Write your code here
    cu=0
    cd=0
    valley_count=0
    pvc=False
    for i in range(steps):
        if path[i]=="U":
            cu+=1
            if cu==cd:
                if pvc:
                    valley_count+=1
                    pvc=False
                cu,cd=0,0
            elif cd>cu:
                pvc=True
                
        elif path[i]=="D":
            cd+=1
            if cu==cd:
                if pvc:
                    valley_count+=1
                    pvc=False
                cu,cd=0,0
            elif cd>cu:
                pvc=True
                    
    return valley_count