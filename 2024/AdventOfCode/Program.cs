using System.IO;

string[] lines = File.ReadAllLines("C:/Users/Matty/Desktop/Coding/hobby/Advent Of Code/2024/Inputs/input1.txt");

// day1Part1(lines);
day1Part2(lines);

void day1Part1(string[] input){
    int[] list1 = new int[lines.Length];
    int[] list2 = new int[lines.Length];

    for(int i = 0; i < lines.Length; i++){
        string[] numbers = lines[i].Split("   ");
        list1[i] = Int32.Parse(numbers[0]);
        list2[i] = Int32.Parse(numbers[1]);
    }

    Array.Sort(list1);
    Array.Sort(list2);

    float difference = 0;

    for(int i = 0; i < list1.Length; i++){
        difference += MathF.Abs(list1[i]-list2[i]);
    }

    Console.WriteLine(difference);
}

void day1Part2(string[] input){
    int[] list1 = new int[lines.Length];
    int[] list2 = new int[lines.Length];

    Dictionary<int,int> instancesOfNumber = new Dictionary<int, int>();

    for(int i = 0; i < lines.Length; i++){
        string[] numbers = lines[i].Split("   ");
        list1[i] = Int32.Parse(numbers[0]);
        list2[i] = Int32.Parse(numbers[1]);

        if (instancesOfNumber.ContainsKey(list2[i])){
            instancesOfNumber[list2[i]] = instancesOfNumber[list2[i]] + 1;
        }else{
            instancesOfNumber[list2[i]] = 1;
        }
    }

    int similarity = 0;

    for(int i = 0; i < list1.Length; i++){
        if (instancesOfNumber.ContainsKey(list1[i])){
            similarity += list1[i] * instancesOfNumber[list1[i]];
        }
    }

    Console.WriteLine(similarity);
} 