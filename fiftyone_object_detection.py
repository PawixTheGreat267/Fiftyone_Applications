import fiftyone as fo
import fiftyone.zoo as foz

def main():
    try:
        # Load the dataset
        dataset = foz.load_zoo_dataset(
            "coco-2017",
            split="validation", 
            dataset_name="evaluate-detections-tutorial",
        )
        dataset.persistent = True

        # Print some information about the dataset
        print(dataset)

        # Print a ground truth detection
        sample = dataset.first()
        print(sample.ground_truth.detections[0])

        # Launch the app
        session = fo.launch_app(dataset)

        # Choose a random subset of 100 samples to add predictions to
        predictions_view = dataset.take(100, seed=51)

        # Load a pre-trained model from the zoo
        model = foz.load_zoo_model("faster-rcnn-resnet50-fpn-coco-torch")
        
        # Apply the model to make predictions
        predictions_view.apply_model(model, label_field="faster_rcnn")

        # Update the session view
        session.view = predictions_view
        
        # Keep the session running
        try:
            session.wait()
        except KeyboardInterrupt:
            print("\nSession stopped.")
            
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Make sure MongoDB is running and FiftyOne is properly configured.")

if __name__ == "__main__":
    main()