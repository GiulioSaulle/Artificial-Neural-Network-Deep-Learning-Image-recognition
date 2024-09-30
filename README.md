<body>
    <h1>AN2DL Challenge 1 - Neural Network Leaf Classification</h1>
    <h2>Introduction</h2>
    <p>The objective of this project is to develop a neural network model that classifies low-resolution images of different types of leaves based on their health status. Each leaf is classified as either <strong>healthy</strong> (0) or <strong>unhealthy</strong> (1).
    </p>
    <p>For extensive information about the task: <a href="https://codalab.lisn.upsaclay.fr/competitions/16245" target="_blank">AN2DL Challenge 1 competition</a></p>
    <h2>First Approach</h2>
    <h3>Input/Output Handling</h3>
    <p>The model was designed to output a tensor of dimension [BS], where BS is the batch size (2), and the input conforms to the model’s inner requirements (e.g., ConvNeXt accepts values in the range of [0-255], with internal normalization).</p>
    <h3>Dataset Analysis</h3>
    <p>The initial dataset included 5200 images (96x96x3 pixels in RGB format), of which 3199 were classified as healthy and 2001 as unhealthy. After cleaning and removing duplicates, we had 4850 images: 3060 healthy and 1790 unhealthy.</p>
    <h3>Imbalance Handling</h3>
    <p>To handle dataset imbalance, we experimented with three techniques:</p>
    <ul>
        <li><strong>Oversampling:</strong> Duplicating minority class images and applying light geometric transformations.</li>
        <li><strong>Undersampling:</strong> Reducing the over-represented class.</li>
        <li><strong>Class Weights:</strong> Assigning higher weights to the minority class.</li>
    </ul>
    <p>We settled on the <strong>Class Weights</strong> technique for its simplicity and effectiveness.</p>
    <h3>Data Splitting</h3>
    <p>We tested various splits of the dataset (e.g., 70/15/15, 90/5/5), with the best results using a (80/10/10) split for train, validation, and test sets.</p>
    <h2>Custom CNN Model</h2>
    <p>We started by implementing a custom Convolutional Neural Network (CNN) from scratch. The final version included two blocks with convolutional layers, followed by an inception layer with multiple branches (1x1, 3x3, 5x5, 7x7 convolutions, and max pooling). Despite some success, data augmentation and further modifications (e.g., adding fully connected layers and LeakyReLU activation) improved accuracy, reaching 67% on the test set.</p>
    <h2>Transfer Learning and Fine-Tuning</h2>
    <p>We adopted Transfer Learning using pre-trained models (MobileNet, EfficientNet, Xception, ConvNeXt). The ConvNeXt model provided the best results (0.89 accuracy). Fine-tuning by unfreezing some layers further enhanced performance.</p>
    <h3>Augmentation Methods</h3>
    <p>The most effective augmentation techniques were:</p>
    <ul>
        <li>Horizontal and Vertical Flip</li>
        <li>Random Rotation and Zoom (0.2)</li>
        <li>Contrast and Brightness Adjustment (0.2)</li>
        <li>RandAugment (KerasCV)</li>
    </ul>
    <h2>Final Model and Hyperparameter Tuning</h2>
    <p>Our best-performing model used ConvNeXt with the following hyperparameters:</p>
    <ul>
        <li><strong>Batch Size:</strong> 128</li>
        <li><strong>Epochs:</strong> 400 (with Early Stopping)</li>
        <li><strong>Learning Rate:</strong> Decreasing from 1e-3 to 1e-5 over time</li>
        <li><strong>Dropout Rate:</strong> 0.2</li>
        <li><strong>Regularizer:</strong> L2 (Ridge Regression)</li>
        <li><strong>Activation Function:</strong> GELU</li>
        <li><strong>Label Smoothing:</strong> 0.15</li>
    </ul>
    <h2>Conclusion</h2>
    <p>The final ConvNeXt model achieved an accuracy of 87.70% in the AN2DL competition. Alongside this model, we also experimented with custom CNNs and other variants, with varying degrees of success.</p>
    <h3>Contribution</h3>
    <p>The project involved contributions from all team members in different stages of model development, testing, and fine-tuning.</p>
</body>
    <p><strong>Authors:</strong> Francesco Colabene, Andrea Gerosa, Christian Lisi, Giulio Saulle</p>
</html>
