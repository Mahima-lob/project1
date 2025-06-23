'''import json
def load_data():
     try:
         with open('youtube','r') as file:
             return json.load(file)
     except FileNotFoundError:
         return[]
     

def save_data_helper(video):
     with open('youtube.txt','w') as file: #we can also use try abd finally concept
          json.dump(video, file)


def list_all_videos(videos):
    for index, viedo in enumerate(videos, start=1):
        print(f"{index}.")
def add_video(video):
    name=input("Enter video name:")
    time=input("Enter video time:")
    video.append({'name': name, 'time': time})
    save_data_helper(video)
def update_video(videos):
        pass

def delete_video(videos):
        pass


def main():#starting point of the program
       videos=load_data()
       while True:
        print("\n Youtube Manager")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. exit from the app")
        choice = input("Enter your choice")
        print(videos)
        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
if __name__ == "__main__":
     main()
    
  '''

import json

# Load data from a file
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist

# Save data to a file
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} | Time: {video['time']}")

# Add a new video
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)
    print("Video added successfully.")

# Update an existing video
def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            videos[index] = {'name': name, 'time': time}
            save_data(videos)
            print("Video updated successfully.")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to delete: ")) - 1
        if 0 <= index < len(videos):
            videos.pop(index)
            save_data(videos)
            print("Video deleted successfully.")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the program
def main():
    videos = load_data()

    while True:
        print("\n===== YouTube Video Manager =====")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_video(videos)
        elif choice == '3':
            update_video(videos)
        elif choice == '4':
            delete_video(videos)
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
