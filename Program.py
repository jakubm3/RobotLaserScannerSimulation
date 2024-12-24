from PIL import Image
from Errors import WrongExtensionError, OutOfRangeError
from Functions import SimulateLaserScanner


def main():
    environment_path = "otoczenie.png"
    params_path = "parametry.txt"

    try:
        print("Starting simulation")
        image_array, line_lengths = (
            SimulateLaserScanner(environment_path, params_path))

        simulation_image = Image.fromarray(image_array)
        simulation_image.save("symulacja.png")
        print("Simulation image saved as 'symulacja.png'")

        with open("wyniki.txt", "w") as file:
            file.write('\n'.join(map(str, line_lengths)))
        print("Line lengths saved to 'wyniki.txt'")

    except WrongExtensionError as e:
        print(f"Error: {e}")
    except OutOfRangeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
