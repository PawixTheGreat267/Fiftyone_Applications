import fiftyone as fo 
import fiftyone.zoo as foz

def main():
    dataset = foz.load_zoo_dataset("quickstart")

    session = fo.launch_app(dataset)

    try:
        session.wait()
    except KeyboardInterrupt:
        print("\nSession stopped.")

if __name__ == "__main__":
    main()