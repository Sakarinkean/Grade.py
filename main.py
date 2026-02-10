# Grade Analyzer Script
# Written in Python for high readability and efficiency

def analyze_grades(scores):
    # Dictionary for mapping score to grade letter
    # Python makes this very clean!
    def get_letter(s):
        if s >= 80: return 'A'
        if s >= 70: return 'B'
        if s >= 60: return 'C'
        if s >= 50: return 'D'
        return 'F'

    # List Comprehension: One of Python's most powerful features
    results = [{"score": s, "grade": get_letter(s)} for s in scores]
    
    # Built-in functions for quick stats
    summary = {
        "count": len(scores),
        "average": sum(scores) / len(scores) if scores else 0,
        "max": max(scores) if scores else 0,
        "min": min(scores) if scores else 0
    }
    
    return results, summary

def main():
    print("--- Python Grade Analytics Tool ---")
    
    # Taking multiple inputs in one line! (Pythonic way)
    raw_input = input("Enter all scores separated by space: ")
    try:
        score_list = [float(x) for x in raw_input.split()]
        
        if not score_list:
            print("No data provided.")
            return

        data, stats = analyze_grades(score_list)

        print("\n[ Detailed Results ]")
        for item in data:
            print(f"Score: {item['score']} -> Grade: {item['grade']}")

        print("\n[ Statistics ]")
        print(f"Total Subjects: {stats['count']}")
        print(f"Average Score : {stats['average']:.2f}")
        print(f"Highest Score : {stats['max']}")
        print(f"Lowest Score  : {stats['min']}")

    except ValueError:
        print("Error: Please enter only numbers!")

if __name__ == "__main__":
    main()