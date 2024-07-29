class Estatistica:
    def media(values: list):
        sum: int = 0;
        count: int = 0;
        for item in values :
            count+1
            sum += item;
        return sum/count;
