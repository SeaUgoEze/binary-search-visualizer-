# Binary Search Algorithm Visualizer

## Demo
![Binary Search Demo](demo.gif)
*Add your screenshot or GIF here after testing*

## Problem Breakdown & Computational Thinking

### Why Binary Search?
I chose **Binary Search** because it's one of the most efficient searching algorithms with O(log n) time complexity. It demonstrates the "divide and conquer" strategy beautifully and is widely used in real-world applications like database indexing and searching in sorted datasets.

### Computational Thinking Framework

#### 1. Decomposition
Binary search breaks down into these smaller steps:
- **Step 1:** Sort the input array (prerequisite)
- **Step 2:** Set left pointer to start (0) and right pointer to end (n-1)
- **Step 3:** Calculate middle index: `mid = (left + right) // 2`
- **Step 4:** Compare middle element with target
- **Step 5:** Adjust search range based on comparison
- **Step 6:** Repeat until target found or range exhausted

#### 2. Pattern Recognition
The algorithm repeatedly:
- Calculates the middle point
- Compares the middle value with the target
- Eliminates half of the remaining elements
- Narrows the search space by half each iteration

#### 3. Abstraction
**Details shown to user:**
- Current search range (left and right indices)
- Middle element being compared
- Visual highlighting of active search region
- Decision logic (go left or right)

**Details hidden from user:**
- Internal pointer arithmetic
- Memory addresses
- Low-level array indexing details

#### 4. Algorithm Design Flow

```
┌─────────────────┐
│  User Input     │
│  - Array        │
│  - Target       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Validate Input  │
│ Parse & Convert │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Sort Array    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Initialize      │
│ left = 0        │
│ right = n-1     │
└────────┬────────┘
         │
         ▼
    ┌────────────┐
    │left ≤ right│◄─────┐
    └─────┬──────┘      │
          │ YES         │
          ▼             │
    ┌────────────┐      │
    │mid=(l+r)/2 │      │
    └─────┬──────┘      │
          │             │
          ▼             │
    ┌────────────┐      │
    │arr[mid]==  │      │
    │  target?   │      │
    └──┬────┬────┘      │
   YES │    │ NO        │
       │    ▼           │
       │ ┌──────────┐   │
       │ │arr[mid]< │   │
       │ │ target?  │   │
       │ └──┬───┬───┘   │
       │YES │   │ NO    │
       │    │   │       │
       │    ▼   ▼       │
       │  ┌─┐ ┌─┐       │
       │  │→│ │←│       │
       │  │R│ │L│       │
       │  └┬┘ └┬┘       │
       │   └───┴────────┘
       ▼
┌─────────────────┐
│ Display Result  │
│ - Found/Not     │
│ - Index         │
│ - Steps         │
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   End Output    │
└─────────────────┘
```

**Input:** 
- Datatype: String (comma-separated integers)
- Structure: List of integers (automatically sorted)

**Output:**
- Visual HTML display showing each step
- Highlighted elements indicating search progress
- Final result with index or "not found" message

## Steps to Run

### Local Setup
1. **Clone this repository:**
   ```bash
   git clone <your-github-repo-url>
   cd binary-search-visualizer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   - The app will automatically open at `http://localhost:7860`
   - Or click the link shown in your terminal

### Usage
1. Enter numbers separated by commas in the "Array" field
2. Enter the target number you want to find
3. Click "Search" button
4. Watch the step-by-step visualization

## Hugging Face Link
   🚀 **Live Demo:** https://huggingface.co/spaces/dopeemp/binary-search-visualizer
## Testing & Verification

### Test Cases

#### Test 1: Target Found (Middle)
- **Input:** Array: `10, 20, 30, 40, 50` | Target: `30`
- **Expected:** Found at index 2
- **Result:** ✅ Pass - Found in 1 step

#### Test 2: Target Found (Left Side)
- **Input:** Array: `5, 12, 23, 45, 67, 89, 100` | Target: `12`
- **Expected:** Found at index 1
- **Result:** ✅ Pass - Found in 2 steps

#### Test 3: Target Not Found
- **Input:** Array: `1, 3, 5, 7, 9` | Target: `4`
- **Expected:** Not found
- **Result:** ✅ Pass - Correctly identified as not present

#### Test 4: Single Element Array
- **Input:** Array: `42` | Target: `42`
- **Expected:** Found at index 0
- **Result:** ✅ Pass - Found in 1 step

#### Test 5: Target Greater Than All
- **Input:** Array: `10, 20, 30` | Target: `100`
- **Expected:** Not found
- **Result:** ✅ Pass - Correctly identified

#### Test 6: Invalid Input
- **Input:** Array: `abc, def` | Target: `5`
- **Expected:** Error message
- **Result:** ✅ Pass - Shows error message

#### Test 7: Empty Array
- **Input:** Array: `` (empty) | Target: `5`
- **Expected:** Error message
- **Result:** ✅ Pass - Shows error message

#### Test 8: Large Array
- **Input:** Array: `1,2,3,...,100` | Target: `87`
- **Expected:** Found efficiently
- **Result:** ✅ Pass - Found in 7 steps (log₂100 ≈ 6.64)

### Edge Cases Handled
- ✅ Unsorted input (automatically sorted)
- ✅ Duplicate values
- ✅ Negative numbers
- ✅ Single element
- ✅ Invalid input (non-numeric)
- ✅ Empty array

## Algorithm Implementation Details

### Time Complexity
- **Best Case:** O(1) - Target is at middle
- **Average Case:** O(log n)
- **Worst Case:** O(log n)

### Space Complexity
- O(1) - Only uses a constant amount of extra space

### Key Features
- 🎨 Color-coded visualization (gold for middle, blue for search range)
- 📊 Step-by-step breakdown
- ✅ Input validation and error handling
- 🔢 Automatic array sorting
- 📱 Responsive web interface

## Author & Acknowledgment

**Author:** Sean Ezeocha 
**Student ID:** 20544189  
**Course:** CISC-121  
**Institution:** Queen's University

### Acknowledgments
- Gradio library for the UI framework
- CISC-121 course materials and project guidelines
- VisuAlgo for algorithm visualization inspiration

### Resources Used
- [Gradio Documentation](https://gradio.app/docs/)
- [Python Official Documentation](https://docs.python.org/)
- [Binary Search Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)

---

**License:** MIT  
**Last Updated:** December 2024
