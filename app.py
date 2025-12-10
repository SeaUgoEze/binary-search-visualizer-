import gradio as gr
import time

def binary_search_visualizer(arr_input, target):
    """
    Performs binary search and returns step-by-step visualization
    
    Args:
        arr_input: String of comma-separated numbers
        target: The number to search for
    
    Returns:
        HTML formatted string showing the search process
    """
    
    # Input validation and parsing
    try:
        # Convert input string to list of integers
        arr = [int(x.strip()) for x in arr_input.split(',')]
        target = int(target)
    except ValueError:
        return "<p style='color: red;'>❌ Error: Please enter valid numbers separated by commas.</p>"
    
    # Check if array is empty
    if len(arr) == 0:
        return "<p style='color: red;'>❌ Error: Array cannot be empty.</p>"
    
    # Sort the array (binary search requires sorted array)
    arr.sort()
    
    # Initialize variables
    left = 0
    right = len(arr) - 1
    steps = []
    step_count = 0
    
    # Add initial state
    steps.append(f"<h3>🔍 Binary Search Visualization</h3>")
    steps.append(f"<p><strong>Sorted Array:</strong> {arr}</p>")
    steps.append(f"<p><strong>Target:</strong> {target}</p>")
    steps.append("<hr>")
    
    # Perform binary search with visualization
    while left <= right:
        step_count += 1
        mid = (left + right) // 2
        
        # Create visual representation of current step
        visual = "<div style='font-family: monospace; font-size: 16px;'>"
        visual += f"<p><strong>Step {step_count}:</strong></p>"
        visual += "<p>Array: "
        
        for i in range(len(arr)):
            if i == mid:
                visual += f"<span style='background-color: #FFD700; padding: 2px 8px; margin: 2px; border-radius: 4px;'><strong>[{arr[i]}]</strong></span> "
            elif i >= left and i <= right:
                visual += f"<span style='background-color: #ADD8E6; padding: 2px 8px; margin: 2px; border-radius: 4px;'>{arr[i]}</span> "
            else:
                visual += f"<span style='color: #CCCCCC; padding: 2px 8px; margin: 2px;'>{arr[i]}</span> "
        
        visual += "</p>"
        visual += f"<p>→ Left index: {left}, Right index: {right}, Mid index: {mid}</p>"
        visual += f"<p>→ Comparing: arr[{mid}] = {arr[mid]} with target = {target}</p>"
        
        # Check if target is found
        if arr[mid] == target:
            visual += f"<p style='color: green;'><strong>✅ Found! Target {target} is at index {mid}</strong></p>"
            steps.append(visual + "</div>")
            break
        elif arr[mid] < target:
            visual += f"<p>→ {arr[mid]} < {target}, search RIGHT half</p>"
            steps.append(visual + "</div>")
            left = mid + 1
        else:
            visual += f"<p>→ {arr[mid]} > {target}, search LEFT half</p>"
            steps.append(visual + "</div>")
            right = mid - 1
        
        steps.append("<hr style='border: 1px dashed #CCCCCC;'>")
    
    # If not found
    if left > right:
        steps.append(f"<p style='color: red;'><strong>❌ Not Found! Target {target} is not in the array.</strong></p>")
        steps.append(f"<p>Total steps: {step_count}</p>")
    else:
        steps.append(f"<p>Total steps: {step_count}</p>")
    
    # Combine all steps
    result = "".join(steps)
    return result


# Create Gradio interface
with gr.Blocks(title="Binary Search Visualizer") as demo:
    
    gr.Markdown("""
    # 🔍 Binary Search Algorithm Visualizer
    
    **Binary Search** is an efficient algorithm for finding a target value in a *sorted* array.
    It works by repeatedly dividing the search interval in half.
    
    ### How to use:
    1. Enter a list of numbers separated by commas (they will be automatically sorted)
    2. Enter the target number you want to find
    3. Click "Search" to see the step-by-step visualization
    
    ### Time Complexity: O(log n) 📊
    """)
    
    with gr.Row():
        with gr.Column():
            array_input = gr.Textbox(
                label="Array (comma-separated numbers)",
                placeholder="e.g., 64, 34, 25, 12, 22, 11, 90, 88, 45",
                value="10, 23, 45, 70, 11, 15, 36, 99, 2, 87"
            )
            target_input = gr.Textbox(
                label="Target Number",
                placeholder="e.g., 45",
                value="45"
            )
            search_btn = gr.Button("🔍 Search", variant="primary")
        
    output = gr.HTML(label="Search Visualization")
    
    # Example inputs
    gr.Markdown("### 📝 Try these examples:")
    gr.Examples(
        examples=[
            ["5, 12, 23, 45, 67, 89, 100", "67"],
            ["1, 3, 5, 7, 9, 11, 13, 15, 17, 19", "13"],
            ["100, 200, 300, 400, 500", "350"],
            ["2, 4, 6, 8, 10, 12, 14, 16, 18, 20", "1"]
        ],
        inputs=[array_input, target_input]
    )
    
    search_btn.click(
        fn=binary_search_visualizer,
        inputs=[array_input, target_input],
        outputs=output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()