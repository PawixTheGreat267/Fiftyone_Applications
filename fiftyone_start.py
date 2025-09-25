import fiftyone as fo 
import fiftyone.zoo as foz

def main():
    dataset = foz.load_zoo_dataset("quickstart")

    session = fo.launch_app(dataset)

    try:
        session.wait()
    except KeyboardInterrupt:
        print("\nSession stopped.")

    session.view = dataset.sort_by("uniqueness").limit(10)

    ##CREATING A GROUP
    # dataset = foz.load_zoo_dataset("quickstart-groups")
    # group_id = dataset.last().group.id

    # session = fo.launch_app(dataset, group_id=group_id)

    
if __name__ == "__main__":
    main()