## Installation

`pip install git+https://github.com/lee-ju/Statistical_Quality_Control.git`

## Usage: SQC_chart

#### Load Package
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Statistical_Quality_Control import SQC_chart
```
#### Example data
- `Source`: Montgomery, D. C. (2007). Introduction to statistical quality control. John Wiley & Sons.
    1. `Wafer0.csv`: Table 6.1
    2. `Orange0.csv`: Table 7.1
    3. `Circuit0.csv`: Table 7.7
    4. `Chain0.csv`: Table 7.10

#### Example for Variables Control Chart: Xbar-R Chart
```python
D = pd.read_csv('.../Wafer0.csv')
xR_M, xR_UCL, xR_LCL = SQC_chart.xbar_R_chart(D=D, A2=0.577) # when n = 5
print(xR_M, xR_UCL, xR_LCL)
```
- `D` and `A2` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as wafer0.csv).
    2. `A2`: Factor for Xbar-R Chart.

#### Example for Variables Control Chart: R Chart
```python
D = pd.read_csv('.../Wafer0.csv')
R_R, R_UCL, R_LCL = SQC_chart.R_chart(D=D, D3=0, D4=2.114) # when n = 5
print(R_R, R_UCL, R_LCL)
```
- `D`, `D3`, and `D4` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as wafer0.csv).
    2. `D3`: Factor of LCL for R Chart.
    3. `D4`: Factor of UCL for R Chart.

#### Example for Variables Control Chart: Xbar-s Chart
```python
D = pd.read_csv('.../Wafer0.csv')
xs_M, xs_UCL, xs_LCL = SQC_chart.xbar_s_chart(D=D, A3=1.427) # when n = 5
print(xs_M, xs_UCL, xs_LCL)
```
- `D` and `A3` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as wafer0.csv).
    2. `A3`: Factor for Xbar-s Chart.

#### Example for Variables Control Chart: s Chart
```python
D = pd.read_csv('.../Wafer0.csv')
s_s, s_UCL, s_LCL = SQC_chart.s_chart(D=D, B3=0, B4=2.089) # when n = 5
print(s_s, s_UCL, s_LCL)
```
- `D`, `B3`, and `B4` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as wafer0.csv).
    2. `B3`: Factor of LCL for s Chart.
    3. `B4`: Factor of UCL for s Chart.

#### Example for Attributes Control Chart: p Chart
```python
D = pd.read_csv('.../Orange0.csv')
pbar, p_UCL, p_LCL = SQC_chart.p_chart(D=D, n=50, var='pi')
print(pbar, p_UCL, p_LCL)
```
- `D`, `n`, and `var` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as Orange0.csv).
    2. `n`: Number of Bernoulli trials.
    3. `var`: The name of the variable representing "sample fraction nonconforming" in D (default: 'pi')

#### Example for Attributes Control Chart: np Chart
```python
D = pd.read_csv('.../Orange0.csv')
npbar, np_UCL, np_LCL = SQC_chart.np_chart(D=D, n=50, var='pi')
print(npbar, np_UCL, np_LCL)
```
- `D`, `n`, and `var` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as Orange0.csv).
    2. `n`: Number of Bernoulli trials.
    3. `var`: The name of the variable representing "sample fraction nonconforming" in D (default: 'pi') 

#### Example for Attributes Control Chart: c Chart
```python
D = pd.read_csv('.../Circuit0.csv')
cbar, c_UCL, c_LCL = SQC_chart.c_chart(D=D, var='N')
print(cbar, c_UCL, c_LCL)
```
- `D` and `var` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as Circuit0.csv).
    2. `var`: The name of the variable representing "number of nonconformities" in D (default: 'N')

#### Example for Attributes Control Chart: u Chart
```python
D = pd.read_csv('.../Chain0.csv')
ubar, u_UCL, u_LCL = SQC_chart.u_chart(D=D, n=50, var='avg_err')
print(ubar, u_UCL, u_LCL)
```
- `D`, `n`, and `var` meaning:
    1. `D`: Data to visualize the chart (must be in the same format as Chain0.csv).
    2. `n`: Number of samples
    3. `var`: The name of the variable representing "average number of erros" in D (default: 'avg_err')

## Usage: Tools

#### Load Package
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils.multiclass import unique_labels

from Statistical_Quality_Control import Tools
```
#### Example: plot_confusion_matrix
```python
from tensorflow.keras.datasets import mnist
(trn_X, trn_y), (tst_X, tst_y) = mnist.load_data()

trn_y_oh = to_categorical(trn_y) # one-hot encoding
tst_y_oh = to_categorical(tst_y)

trn_X = trn_X / 255.0
tst_X = tst_X / 255.0

trn_X = trn_X.reshape(trn_n, trn_d * trn_d) # 60000 x 28 -> 60000 x 784
tst_X = tst_X.reshape(tst_n, trn_d * trn_d)

input_X = Input(shape=(trn_d * trn_d,)) # 784
hidden1 = Dense(256, activation='relu')(input_X)
hidden2 = Dense(64, activation='relu')(hidden1)
hidden3 = Dense(16, activation='relu')(hidden2)
output = Dense(10, activation='softmax')(hidden3)

dnn_clf = Model(input_X, output)
dnn_clf.compile(loss='categorical_crossentropy',
                metrics=['accuracy'])
                
history = dnn_clf.fit(trn_X, trn_y_oh, epochs=10, batch_size=256)

pred_y = dnn_clf.predict(tst_X)
Tools.plot_confusion_matrix(y_true=tst_y, y_pred=np.argmax(pred_y, axis=1),
                            classes=['0','1','2','3','4','5','6','7','8','9'],
                            title='Confusion matrix of DNN')
```
- `y_true`, `y_pred`, `classes`, and `title` meaning:
    1. `y_true`: Ground truth (correct) target values. array-like of shape (n_samples,)
    2. `y_pred`: Estimated targets as returned by a classifier. array-like of shape (n_samples,)
    3. `classes` : List of labels to index the matrix. array-like of shape (n_classes)
    4. `title` : Title of confusion matrix. string

## Statistical_Quality_Control

#### 2022-01 SQC Colab Env
#### !pip freeze
#### absl-py==1.0.0
#### alabaster==0.7.12
#### albumentations==0.1.12
#### altair==4.2.0
#### appdirs==1.4.4
#### argon2-cffi==21.3.0
#### argon2-cffi-bindings==21.2.0
#### arviz==0.11.4
#### astor==0.8.1
#### astropy==4.3.1
#### astunparse==1.6.3
#### atari-py==0.2.9
#### atomicwrites==1.4.0
#### attrs==21.4.0
#### audioread==2.1.9
#### autograd==1.3
#### Babel==2.9.1
#### backcall==0.2.0
#### beautifulsoup4==4.6.3
#### bleach==4.1.0
#### blis==0.4.1
#### bokeh==2.3.3
#### Bottleneck==1.3.2
#### branca==0.4.2
#### bs4==0.0.1
#### CacheControl==0.12.10
#### cached-property==1.5.2
#### cachetools==4.2.4
#### catalogue==1.0.0
#### certifi==2021.10.8
#### cffi==1.15.0
#### cftime==1.5.2
#### chardet==3.0.4
#### charset-normalizer==2.0.11
#### click==7.1.2
#### cloudpickle==1.3.0
#### cmake==3.12.0
#### cmdstanpy==0.9.5
#### colorcet==3.0.0
#### colorlover==0.3.0
#### community==1.0.0b1
#### contextlib2==0.5.5
#### convertdate==2.4.0
#### coverage==3.7.1
#### coveralls==0.5
#### crcmod==1.7
#### cufflinks==0.17.3
#### cvxopt==1.2.7
#### cvxpy==1.0.31
#### cycler==0.11.0
#### cymem==2.0.6
#### Cython==0.29.26
#### daft==0.0.4
#### dask==2.12.0
#### datascience==0.10.6
#### debugpy==1.0.0
#### decorator==4.4.2
#### defusedxml==0.7.1
#### descartes==1.1.0
#### dill==0.3.4
#### distributed==1.25.3
#### dlib @ file:///dlib-19.18.0-cp37-cp37m-linux_x86_64.whl
#### dm-tree==0.1.6
#### docopt==0.6.2
#### docutils==0.17.1
#### dopamine-rl==1.0.5
#### earthengine-api==0.1.296
#### easydict==1.9
#### ecos==2.0.10
#### editdistance==0.5.3
#### en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.5/en_core_web_sm-2.2.5.tar.gz
#### entrypoints==0.3
#### ephem==4.1.3
#### et-xmlfile==1.1.0
#### fa2==0.3.5
#### fastai==1.0.61
#### fastdtw==0.3.4
#### fastprogress==1.0.0
#### fastrlock==0.8
#### fbprophet==0.7.1
#### feather-format==0.4.1
#### filelock==3.4.2
#### firebase-admin==4.4.0
#### fix-yahoo-finance==0.0.22
#### Flask==1.1.4
#### flatbuffers==2.0
#### folium==0.8.3
#### future==0.16.0
#### gast==0.4.0
#### GDAL==2.2.2
#### gdown==4.2.0
#### gensim==3.6.0
#### geographiclib==1.52
#### geopy==1.17.0
#### gin-config==0.5.0
#### glob2==0.7
#### google==2.0.3
#### google-api-core==1.26.3
#### google-api-python-client==1.12.10
#### google-auth==1.35.0
#### google-auth-httplib2==0.0.4
#### google-auth-oauthlib==0.4.6
#### google-cloud-bigquery==1.21.0
#### google-cloud-bigquery-storage==1.1.0
#### google-cloud-core==1.0.3
#### google-cloud-datastore==1.8.0
#### google-cloud-firestore==1.7.0
#### google-cloud-language==1.2.0
#### google-cloud-storage==1.18.1
#### google-cloud-translate==1.5.0
#### google-colab @ file:///colabtools/dist/google-colab-1.0.0.tar.gz
#### google-pasta==0.2.0
#### google-resumable-media==0.4.1
#### googleapis-common-protos==1.54.0
#### googledrivedownloader==0.4
#### graphviz==0.10.1
#### greenlet==1.1.2
#### grpcio==1.43.0
#### gspread==3.4.2
#### gspread-dataframe==3.0.8
#### gym==0.17.3
#### h5py==3.1.0
#### HeapDict==1.0.1
#### hijri-converter==2.2.2
#### holidays==0.10.5.2
#### holoviews==1.14.7
#### html5lib==1.0.1
#### httpimport==0.5.18
#### httplib2==0.17.4
#### httplib2shim==0.0.3
#### humanize==0.5.1
#### hyperopt==0.1.2
#### ideep4py==2.0.0.post3
#### idna==2.10
#### imageio==2.4.1
#### imagesize==1.3.0
#### imbalanced-learn==0.8.1
#### imblearn==0.0
#### imgaug==0.2.9
#### importlib-metadata==4.10.1
#### importlib-resources==5.4.0
#### imutils==0.5.4
#### inflect==2.1.0
#### iniconfig==1.1.1
#### intel-openmp==2022.0.2
#### intervaltree==2.1.0
#### ipykernel==4.10.1
#### ipython==5.5.0
#### ipython-genutils==0.2.0
#### ipython-sql==0.3.9
#### ipywidgets==7.6.5
#### itsdangerous==1.1.0
#### jax==0.2.25
#### jaxlib @ https://storage.googleapis.com/jax-releases/cuda111/jaxlib-0.1.71+cuda111-cp37-none-manylinux2010_x86_64.whl
#### jdcal==1.4.1
#### jedi==0.18.1
#### jieba==0.42.1
#### Jinja2==2.11.3
#### joblib==1.1.0
#### jpeg4py==0.1.4
#### jsonschema==4.3.3
#### jupyter==1.0.0
#### jupyter-client==5.3.5
#### jupyter-console==5.2.0
#### jupyter-core==4.9.1
#### jupyterlab-pygments==0.1.2
#### jupyterlab-widgets==1.0.2
#### kaggle==1.5.12
#### kapre==0.3.7
#### keras==2.7.0
#### Keras-Preprocessing==1.1.2
#### keras-vis==0.4.1
#### kiwisolver==1.3.2
#### korean-lunar-calendar==0.2.1
#### libclang==13.0.0
#### librosa==0.8.1
#### lightgbm==2.2.3
#### llvmlite==0.34.0
#### lmdb==0.99
#### LunarCalendar==0.0.9
#### lxml==4.2.6
#### Markdown==3.3.6
#### MarkupSafe==2.0.1
#### matplotlib==3.2.2
#### matplotlib-inline==0.1.3
#### matplotlib-venn==0.11.6
#### missingno==0.5.0
#### mistune==0.8.4
#### mizani==0.6.0
#### mkl==2019.0
#### mlxtend==0.14.0
#### more-itertools==8.12.0
#### moviepy==0.2.3.5
#### mpmath==1.2.1
#### msgpack==1.0.3
#### multiprocess==0.70.12.2
#### multitasking==0.0.10
#### murmurhash==1.0.6
#### music21==5.5.0
#### natsort==5.5.0
#### nbclient==0.5.10
#### nbconvert==5.6.1
#### nbformat==5.1.3
#### nest-asyncio==1.5.4
#### netCDF4==1.5.8
#### networkx==2.6.3
#### nibabel==3.0.2
#### nltk==3.2.5
#### notebook==5.3.1
#### numba==0.51.2
#### numexpr==2.8.1
#### numpy==1.19.5
#### nvidia-ml-py3==7.352.0
#### oauth2client==4.1.3
#### oauthlib==3.1.1
#### okgrade==0.4.3
#### opencv-contrib-python==4.1.2.30
#### opencv-python==4.1.2.30
#### openpyxl==2.5.9
#### opt-einsum==3.3.0
#### osqp==0.6.2.post0
#### packaging==21.3
#### palettable==3.3.0
#### pandas==1.3.5
#### pandas-datareader==0.9.0
#### pandas-gbq==0.13.3
#### pandas-profiling==1.4.1
#### pandocfilters==1.5.0
#### panel==0.12.1
#### param==1.12.0
#### parso==0.8.3
#### pathlib==1.0.1
#### patsy==0.5.2
#### pep517==0.12.0
#### pexpect==4.8.0
#### pickleshare==0.7.5
#### Pillow==7.1.2
#### pip-tools==6.2.0
#### plac==1.1.3
#### plotly==5.5.0
#### plotnine==0.6.0
#### pluggy==0.7.1
#### pooch==1.6.0
#### portpicker==1.3.9
#### prefetch-generator==1.0.1
#### preshed==3.0.6
#### prettytable==3.0.0
#### progressbar2==3.38.0
#### prometheus-client==0.13.1
#### promise==2.3
#### prompt-toolkit==1.0.18
#### protobuf==3.17.3
#### psutil==5.4.8
#### psycopg2==2.7.6.1
#### ptyprocess==0.7.0
#### py==1.11.0
#### pyarrow==3.0.0
#### pyasn1==0.4.8
#### pyasn1-modules==0.2.8
#### pycocotools==2.0.4
#### pycparser==2.21
#### pyct==0.4.8
#### pydata-google-auth==1.3.0
#### pydot==1.3.0
#### pydot-ng==2.0.0
#### pydotplus==2.0.2
#### PyDrive==1.3.1
#### pyemd==0.5.1
#### pyerfa==2.0.0.1
#### pyglet==1.5.0
#### Pygments==2.6.1
#### pygobject==3.26.1
#### pymc3==3.11.4
#### PyMeeus==0.5.11
#### pymongo==4.0.1
#### pymystem3==0.2.0
#### PyOpenGL==3.1.5
#### pyparsing==3.0.7
#### pyrsistent==0.18.1
#### pysndfile==1.3.8
#### PySocks==1.7.1
#### pystan==2.19.1.1
#### pytest==3.6.4
#### python-apt==0.0.0
#### python-chess==0.23.11
#### python-dateutil==2.8.2
#### python-louvain==0.15
#### python-slugify==5.0.2
#### python-utils==3.1.0
#### pytz==2018.9
#### pyviz-comms==2.1.0
#### PyWavelets==1.2.0
#### PyYAML==3.13
#### pyzmq==22.3.0
#### qdldl==0.1.5.post0
#### qtconsole==5.2.2
#### QtPy==2.0.0
#### regex==2019.12.20
#### requests==2.23.0
#### requests-oauthlib==1.3.0
#### resampy==0.2.2
#### rpy2==3.4.5
#### rsa==4.8
#### scikit-image==0.18.3
#### scikit-learn==1.0.2
#### scipy==1.4.1
#### screen-resolution-extra==0.0.0
#### scs==3.1.0
#### seaborn==0.11.2
#### semver==2.13.0
#### Send2Trash==1.8.0
#### setuptools-git==1.2
#### Shapely==1.8.0
#### simplegeneric==0.8.1
#### six==1.15.0
#### sklearn==0.0
#### sklearn-pandas==1.8.0
#### smart-open==5.2.1
#### snowballstemmer==2.2.0
#### sortedcontainers==2.4.0
#### SoundFile==0.10.3.post1
#### spacy==2.2.4
#### Sphinx==1.8.6
#### sphinxcontrib-serializinghtml==1.1.5
#### sphinxcontrib-websupport==1.2.4
#### SQLAlchemy==1.4.31
#### sqlparse==0.4.2
#### srsly==1.0.5
#### statsmodels==0.10.2
#### sympy==1.7.1
#### tables==3.4.4
#### tabulate==0.8.9
#### tblib==1.7.0
#### tenacity==8.0.1
#### tensorboard==2.7.0
#### tensorboard-data-server==0.6.1
#### tensorboard-plugin-wit==1.8.1
#### tensorflow @ file:///tensorflow-2.7.0-cp37-cp37m-linux_x86_64.whl
#### tensorflow-datasets==4.0.1
#### tensorflow-estimator==2.7.0
#### tensorflow-gcs-config==2.7.0
#### tensorflow-hub==0.12.0
#### tensorflow-io-gcs-filesystem==0.23.1
#### tensorflow-metadata==1.6.0
#### tensorflow-probability==0.15.0
#### termcolor==1.1.0
#### terminado==0.13.1
#### testpath==0.5.0
#### text-unidecode==1.3
#### textblob==0.15.3
#### Theano-PyMC==1.1.2
#### thinc==7.4.0
#### threadpoolctl==3.0.0
#### tifffile==2021.11.2
#### toml==0.10.2
#### tomli==2.0.0
#### toolz==0.11.2
