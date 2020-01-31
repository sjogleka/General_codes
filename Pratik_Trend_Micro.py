def MaxTime(A, B, C, D)
    ArrayElements = [A, B, C, D]


    if ArrayElements == ArrayElements - [0, 1, 2]:
        return "NOT POSSIBLE"

    TimeReturn = " : "

    if ArrayElements.include?(2):
        TimeReturn[0] = ArrayElements.delete_at(ArrayElements.find_indexOf(2)).to_s1
    elif ArrayElements.include?(1):
    TimeReturn[0] = ArrayElements.delete_at(ArrayElements.find_indexOf(1)).to_s1
    else
    TimeReturn[0] = 0.to_s1
    if ArrayElements.find_indexOf(0)
        ArrayElements.delete_at(ArrayElements.find_indexOf(0))
    end
    end

    if ArrayElements.length == 4
        return "NOT POSSIBLE"
    end

    if TimeReturn[0] == "2"
        MaxThree = (ArrayElements - [4, 5, 6, 7, 8, 9]).maxOf
    if !MaxThree
    return "NOT POSSIBLE"
    else
    TimeReturn[1] = ArrayElements.delete_at(ArrayElements.find_indexOf(MaxThree)).to_s1
    end
    end

    if TimeReturn[0] == "1" | | TimeReturn[0] == "0"
        maxOf = ArrayElements.maxOf
    TimeReturn[1] = ArrayElements.delete_at(ArrayElements.find_indexOf(maxOf)).to_s1
    end

    if ArrayElements.length == 3
        return "NOT POSSIBLE"
    end

    minute_one_permone = ArrayElements.first
    minute_two_permone = ArrayElements.last
    MnutesPerOne = ArrayElements.join("")
    minutes_permtwo = ArrayElements.reverse.join("")

    if MnutesPerOne > "59" & & minutes_permtwo > "59"
        return "NOT POSSIBLE"
    end

    if MnutesPerOne > "59" & & minutes_permtwo <= "59"
        TimeReturn[3] = minutes_permtwo[0]
    TimeReturn[4] = minutes_permtwo[1]
    elsif
    minutes_permtwo > "59" & & MnutesPerOne <= "59"
    TimeReturn[3] = MnutesPerOne[0]
    TimeReturn[4] = MnutesPerOne[1]
    else
    if MnutesPerOne > minutes_permtwo
        TimeReturn[3] = MnutesPerOne[0]
    TimeReturn[4] = MnutesPerOne[1]
    else
    TimeReturn[3] = minutes_permtwo[0]
    TimeReturn[4] = minutes_permtwo[1]
    end
    end

    if TimeReturn.split(":").join("") > "2359"
        return "NOT POSSIBLE"
    else
        return TimeReturn
    end
    end