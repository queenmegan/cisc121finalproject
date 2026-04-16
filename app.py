import gradio as gr
from sympy import div
with gr.Blocks() as demo:
        def parse_input(text):
            """
            Expected format:
            Main Library, 45
            Residence Hall, 20
            Engineering Building, 60
            """
            lines = text.strip().split("\n")
            stops = []

            for line in lines:
                if not line.strip():
                    continue

                parts = line.split(",")

                if len(parts) != 2:
                    raise ValueError("Each line must have exactly one stop name and one crowd count, separated by a comma.")

                stop_name = parts[0].strip()
                crowd_text = parts[1].strip()

                if stop_name == "":
                    raise ValueError("Stop name cannot be empty.")

                if not crowd_text.isdigit():
                    raise ValueError(f"Crowd count for '{stop_name}' must be a whole number.")

                crowd_count = int(crowd_text)

                stops.append({
                    "stop_name": stop_name,
                    "crowd_count": crowd_count
                })

            if len(stops) == 0:
                raise ValueError("Please enter at least one shuttle stop.")
            return stops

# -----------------------------
# Merge sort with step tracking
# -----------------------------
def merge_sort_with_steps(arr, steps):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_with_steps(arr[:mid], steps)
    right = merge_sort_with_steps(arr[mid:], steps)

    return merge(left, right, steps)


def merge(left, right, steps):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["crowd_count"] <= right[j]["crowd_count"]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    # Record this merge step for visualization
    step_text = []
    for item in merged:
        step_text.append(f'{item["stop_name"]} ({item["crowd_count"]})')
    steps.append(step_text)

    return merged


# -----------------------------
# Format results nicely
# -----------------------------
def format_final_ranking(sorted_stops):
    result = "Final Ranked Shuttle Stops:\n\n"
    for index, stop in enumerate(sorted_stops, start=1):
        result += f'{index}. {stop["stop_name"]} - Crowd Count: {stop["crowd_count"]}\n'
    return result


def format_steps(steps):
    output = "Merge Sort Steps:\n\n"
    for i, step in enumerate(steps, start=1):
        output += f"Step {i}: " + " -> ".join(step) + "\n"
    return output


# -----------------------------
# Main app logic
# -----------------------------
def rank_shuttle_stops(user_input):
    try:
        stops = parse_input(user_input)

        steps = []
        sorted_stops = merge_sort_with_steps(stops, steps)

        final_ranking = format_final_ranking(sorted_stops)
        step_output = format_steps(steps)

        return final_ranking, step_output

    except Exception as e:
        return f"Error: {str(e)}", ""


# -----------------------------
# Gradio UI
# -----------------------------
example_input = """Main Library, 45
Residence Hall, 20
Engineering Building, 60
Student Center, 35"""

with gr.Blocks(css="""
.gradio-container {background: #f3e8ff !important; color: white !important;}
.gradio-container label, .gradio-container button, .gradio-container textarea, .gradio-container input {
    color: white !important;
}
.black-text, .black-text * {
    color: black !important;
}
""") as demo:
    with gr.Tab("🎀 MERGE SORT MACHINE "):
        gr.HTML("<div class='black-text'><h1>*¤ଘ* ✧｡･ﾟ✧•Shuttle Stop Crowd Ranking•*｡ଘ* ✧☆･ﾟ✧•</h1></div>")
        gr.HTML("<div class='black-text'><h1>*play some music while sorting!*</h1></div>")
        gr.Audio(
        value="music.mp3",
        autoplay=True,
        loop=True,
        interactive=False,
        show_label=False
        )
        gr.HTML("""
        <div class='black-text'>
            Enter shuttle stop names and crowd counts, one per line, in this format:<br>
            <code>Stop Name, Crowd Count</code><br><br>
            The app uses <b>Merge Sort</b> to rank stops from least crowded to most crowded.
        """)
        input_box = gr.Textbox(
            label="*ଘ* ੈ✩‧₊˚✧*｡Enter Shuttle Stops*｡ଘ* ੈ✩‧₊˚✧*｡",
            lines=8,
            value=example_input
        )
        sort_button = gr.Button("*ଘ* ੈ✩‧₊˚✧*｡Sort Shuttle Stops*｡ଘ* ੈ✩‧₊˚✧*｡")

        output_ranking = gr.Textbox(label="Final Ranking", lines=10)
        output_steps = gr.Textbox(label="Sorting Steps", lines=12)

        sort_button.click(
            fn=rank_shuttle_stops,
            inputs=input_box,
            outputs=[output_ranking, output_steps]
        )
        gr.HTML("<div class='black-text'><h1>yay! you understand the idea of merge sort now!</h1></div>")
        gr.Image(
            value="kuromi.gif",
            interactive=False,
            show_label=False
        )

    with gr.Tab("🩷 WHAT IS MERGE SORT?"):
        gr.HTML("""
     <div style="
            background-color: light purple;
            padding: 50px 40px;
            min-height: 300px;
            text-align: left;
        ">
            <h1 style="
                color: black;
                font-size: 64px;
                font-style: roman;
                font-family: Georgia, serif;
                margin-bottom: 35px;
            ">
                What is Merge Sort?
            </h1>
            
            <m1 style="
                color: black;
                font-size: 28px;
                font-style: roman;
                font-family: Georgia, serif;
                margin-bottom: 80px;
            ">
                Merge Sort is a highly efficient, stable, and comparison-based sorting algorithm that follows the divide-and-conquer paradigm. It works by recursively splitting an unsorted array into smaller subarrays, sorting them, and then merging them back together into a single sorted array.
            </m1>
                </div>
            <p style="
                color: black;
                font-size: 20px;
                font-weight: bold;
                line-height: 1.8;
                max-width: 1700px;
                margin-bottom: 10px;
            ">
                Step 1: Divide: The unsorted list is recursively split in half until each sub-list contains only one element (single element is considered sorted).<br>
                Step 2: Conquer/Sort: The individual elements are merged together, comparing elements from each sub-list and arranging them in sorted order.<br>
                Step 3: Merge: This process of merging sorted smaller lists into larger, sorted lists continues until all elements are recombined into a single sorted list.
            </p>
        </div>
        """)


demo.launch()