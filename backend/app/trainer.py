import os
path = os.path.join(output_dir, 'torch_model.pt')
self.torch.save(self.model.state_dict(), path)
return path




# Training manager
class TrainingManager:
def __init__(self, base_dir='/app'):
self.base_dir = base_dir
self.jobs = {}
self.plugins = {
'keras': KerasPlugin,
'torch': TorchPlugin
}


def enqueue_pipeline(self, spec: dict):
job_id = str(uuid.uuid4())
self.jobs[job_id] = {'spec': spec, 'status': 'queued'}
return job_id


def run_job(self, job_id: str):
job = self.jobs[job_id]
spec = job['spec']
job['status'] = 'running'
# 1. load data
data_path = spec['data'].get('path')
df = pd.read_csv(data_path)
# 2. feature pipeline
X, y, preproc = self._build_features(df, spec['feature_nodes'])
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
# 3. model
model_type = spec['model']['type']
plugin_cls = self.plugins[model_type]
plugin = plugin_cls()
plugin.build(spec['model']['config'])
out_dir = os.path.join(MODEL_DIR, job_id)
os.makedirs(out_dir, exist_ok=True)
plugin.train(X_train, y_train, X_val, y_val, spec.get('training', {}), out_dir)
model_path = plugin.save(out_dir)
# save metadata
save_json(os.path.join(out_dir, 'spec.json'), spec)
# save preprocessor
joblib.dump(preproc, os.path.join(out_dir, 'preprocessor.joblib'))
job['status'] = 'done'
job['model_path'] = model_path
return job


def _build_features(self, df: pd.DataFrame, feat_spec: dict):
# feat_spec: {numeric_cols: [], cat_cols: [], target: str}
numeric_cols = feat_spec.get('numeric_cols', [])
