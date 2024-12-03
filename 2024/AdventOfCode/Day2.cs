class Day2{

    public static void runBoth(){
        string[] input = File.ReadAllLines("C:/Users/Matty/Desktop/Coding/hobby/Advent Of Code/2024/Inputs/input2.txt");
        part1(input);
        part2(input);
    }

    private static bool isSafe(int[] levels){
        int gradient = levels[0] - levels[1];
        bool isGradientPositive = gradient > 0;
        if (Math.Abs(gradient) == 0 || Math.Abs(gradient) > 3){
            return false;
        }
        for(int i = 1; i < levels.Length-1; i++){
            gradient = levels[i] - levels[i+1];
            if (!(gradient > 0 && isGradientPositive || gradient < 0 && !isGradientPositive)){
                return false;
            }
            if (Math.Abs(gradient) == 0 || Math.Abs(gradient) > 3){
                return false;
            }
        }
        return true;
    }
    public static void part1(string[] input){
        int safeReports = 0;
        foreach(string stringReport in input){
            string[] splitReport = stringReport.Split(" ");
            int[] report = new int[splitReport.Length];
            for(int i = 0; i < report.Length; i++){
                report[i] = Int32.Parse(splitReport[i]);
            }
            if (isSafe(report)){
                safeReports++;
            }
        }
        Console.WriteLine(safeReports);
    }

    public static void part2(string[] input){
        int safeReports = 0;
        foreach(string stringReport in input){
            string[] splitReport = stringReport.Split(" ");
            int[] report = new int[splitReport.Length];
            for(int i = 0; i < report.Length; i++){
                report[i] = Int32.Parse(splitReport[i]);
            }
            if (isSafe(report)){
                safeReports++;
            }else{
                for(int i = 0; i < report.Length; i++){
                    int[] subReport = new int[report.Length-1];
                    for(int j = 0, n = 0; j < subReport.Length; n++){
                        if (n == i){
                            continue;
                        }
                        subReport[j] = report[n];
                        j++;
                    }
                    if(isSafe(subReport)){
                        safeReports++;
                        break;
                    }
                }
            }
        }
        Console.WriteLine(safeReports);
    } 
}