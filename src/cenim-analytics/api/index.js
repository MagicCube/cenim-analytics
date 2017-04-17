import { get, post } from '../http/client';


export async function loadMovieClusters() {
  const clusters = await get('/data/clusters-25.json');
  return clusters;
}
