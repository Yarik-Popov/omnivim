
# Omnivim

  

Omnivim is a project developed by 3 high-school students that enhances your developer workflow by integrating global vim motions. 

### Features


- Global Vim motion integration - Use beloved vim motion across any application

- Custom Tray Icons - Icons in the taskbar to quickly indicated what mode you are currently in

- 5 modes - 3 of the original Vim modes, as well as 2 custom ones added in
 - Low resource drain - using less then 1 % of CPU processing power on every machine we tested on

## Using Omnivim
Omnivim is split into 5 modes, being Kill, Insert, Visual, Mouse and Normal mode. Additionally, a GUI can be opened via clicking on the tray icon. All modes have custom key binds and functionalities which are listed below:

### Normal Mode:
- Basic Motion Keys:

	-   **`h`** → Moves the cursor **left** 
	-   **`j`** → Moves the cursor **down** 
	-   **`k`** → Moves the cursor **up** 
	-   **`l`** → Moves the cursor **right** 

- Word and Line Navigation:

	-  **`b`** → Moves the cursor **one word left** 
	-   **`w`** → Moves the cursor **one word right** 
	-   **`0`** → Moves the cursor **to the beginning of the line**
	-   **`^`** → Moves the cursor **to the first non-whitespace character** on the line 
	-   **`$`** → Moves the cursor **to the end of the line** 
	-   **`G`** → Moves the cursor **to the end of the document** 
	-   **`g g`** → Moves the cursor **to the beginning of the document** 

- Editing Commands:
	-   **`d`** → Activates **delete mode** 
	-   **`d d`** → Deletes the **entire line** 
	-   **`d w`** → Deletes the next **word** 

- Text Manipulation:

	-   **`x`** → Deletes **a single character** 
	-   **`p`** → **Paste** clipboard content 
	-   **`o`** → Opens a **new line below** and enters insert mode
	-   **`O`** → Opens a **new line above** and enters insert mode
	-   **`u`** → **Undoes** the last action 
	-   **`r`** → **Redoes** the last undone action
  
  ### Visual Mode:
note that all motions will highlight text in Visual mode.
-   Basic Motion Keys:
    
    -   **`h`** → Expands selection **left**
    -   **`j`** → Expands selection **down**
    -   **`k`** → Expands selection **up**
    -   **`l`** → Expands selection **right**
-   Word and Line Navigation:
    
    -   **`b`** → Expands selection **one word left**
    -   **`w`** → Expands selection **one word right**
    -   **`0`** → Expands selection **to the beginning of the line** 
    -   **`^`** → Expands selection **to the first non-whitespace character** on the line
    -   **`$`** → Expands selection **to the end of the line**
    -   **`G`** → Expands selection **to the end of the document**
    -   **`g g`** → Expands selection **to the beginning of the document**
-   Editing Commands:
    
    -   **`y`** → **Yank (copy)** selection and reset cursor position
    -   **`x`** → **Delete** selection and exit Visual Mode
   -   Entering Other Modes:
    
	    -   **`i`** → Goes to **Insert mode**
	    -   **`m`** → Goes to **Mouse mode**
	    -   **`v`** → Goes to **Visual mode**
	    -   **`Ctrl + Shift + q`** → Goes to **Kill mode**
  
### Mouse Mode:

-   Cursor Movement:
    
    -   **`h`** → Moves the mouse **left**
    -   **`l`** → Moves the mouse **right**
    -   **`k`** → Moves the mouse **up**
    -   **`j`** → Moves the mouse **down**
    -   **`H`** → Moves the mouse **left (fast)**
    -   **`L`** → Moves the mouse **right (fast)**
    -   **`K`** → Moves the mouse **up (fast)**
    -   **`J`** → Moves the mouse **down (fast)**
-   Scrolling:
    
    -   **`u`** → Scroll **up**
    -   **`i`** → Scroll **down**
    -   **`U`** → Scroll **up (fast)**
    -   **`I`** → Scroll **down (fast)**

-   Segment-based Mouse Positioning:
    
    -   **`q`** → Moves mouse to **top-left segment**
    -   **`w`** → Moves mouse to **top-center-left segment**
    -   **`e`** → Moves mouse to **top-center-right segment**
    -   **`r`** → Moves mouse to **top-right segment**
    -   **`a`** → Moves mouse to **middle-left segment**
    -   **`s`** → Moves mouse to **middle-center-left segment**
    -   **`d`** → Moves mouse to **middle-center-right segment**
    -   **`f`** → Moves mouse to **middle-right segment**
    -   **`z`** → Moves mouse to **bottom-left segment**
    -   **`x`** → Moves mouse to **bottom-center-left segment**
    -   **`c`** → Moves mouse to **bottom-center-right segment**
    -   **`v`** → Moves mouse to **bottom-right segment**
-   Mouse Clicks:
    
    -   **`space`** → **Left click**
    -   **`n`** → **Right click**
   -   Exiting Insert Mode:
    
	    -   **Esc** → Returns to **Normal Mode**
	    -   **Ctrl + C** → Returns to **Normal Mode**
### **Insert Mode**:

-   Typing & Navigation:
    
    -   **`All standard key inputs`** → Works as expected
    -   **`Shift + letter`** → Inserts **uppercase letter**
    -   **`Arrow keys`** → Moves cursor (handled with shift compatibility)
-   Control Modifiers:
 
    -   **`Ctrl + any key`** → Passes the input normally
    -   **`Ctrl + Shift + key`** → Passes the input normally
-   Exiting Insert Mode:
    
    -   **`Esc`** → Returns to **Normal Mode**
    -   **`Ctrl + C`** → Returns to **Normal Mode**


### **Kill Mode (Off Mode)**:

-   Used for disabling Omnivim keybindings
-   **`Ctrl + Shift + q`** → Toggles between **Kill Mode** and **Normal Mode**
-   In Kill Mode, all key inputs work as default (except for anything bound to **`Ctrl + Shift + q`**
## Installation

  

To set up Omnivim on your system, follow these steps:

  

### Clone the Repository

```bash
git clone https://github.com/derekGou/omnivim.git
```

### Navigate to the Project Directory

```bash
cd omnivim
```

### Windows Setup

```bash
build.bat
setup.bat
```
  

### Linux Setup

```bash
sudo apt-get install python3-pip python3-tk python3-dev libxcb-cursor0  # Install dependencies
./build.sh
```

## Usage

  

After installation, launch Omnivim by executing the exe in `\dist`

## GUI
We built a simple, clean interface launched through the tray icon for users to toggle and test Omnivim. Additionally, the tray icon displays the current mode being used. ![](https://cdn.discordapp.com/attachments/1342874659326132225/1343218148115091508/Screenshot202025-02-2320at208.png?ex=67bc78e2&is=67bb2762&hm=2cc460c9373565d6e2cae21eb50ffede07ec56dda735844a852905e8213d7366&)

## Icon explanation
|  **Off mode** | **Normal** | **Insert** | **Visual** | **Mouse** |
|--|--| -- | --| --|
|![Off mode](https://cdn.discordapp.com/attachments/1342874659326132225/1343218539095527424/omnivimoff.png?ex=67bc793f&is=67bb27bf&hm=e033ec35b541794485dc8c7945fe68e0df36622b789db1ee04c20f83e99ffec1&)| ![Normal](https://cdn.discordapp.com/attachments/1342874659326132225/1343218539422810205/omnivimnormal.png?ex=67bc793f&is=67bb27bf&hm=bce9b9078857b194db8ef588c135997036f54e78590ba1bc18552a9497cc2dc5&) |![Insert](https://cdn.discordapp.com/attachments/1342874659326132225/1343218540022337617/omniviminsert.png?ex=67bc793f&is=67bb27bf&hm=b298163beaabbcd30cde521c99b1b8f0aa44450661d32879b7fc71b6d9b82f62&) | ![Visual](https://cdn.discordapp.com/attachments/1342874659326132225/1343218538776756286/omnivimvisual.png?ex=67bc793f&is=67bb27bf&hm=68560e283cc3cfbb51b0958d7cd3f408a570dbdfcfdca5fdef5222d19179ad5d&) | ![Mouse](https://cdn.discordapp.com/attachments/1342874659326132225/1343218539728998490/omnivimmouse.png?ex=67bc793f&is=67bb27bf&hm=f05ea6f26cd4c88d1285c6c46da9713c30f4fe5b7e21c1d2410114733bbade31&) |
